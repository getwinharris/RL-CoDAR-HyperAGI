#!/usr/bin/env python3
"""
bapX-v1 Crystallization — Based on bapxdi_v3 working code
==========================================================

SIX FORMULAS (from bapxdi_v3):

1. BIT DIFFUSION — angular encoding (2208.04202)
   θ = 2πb/256, diffuse in angle space

2. BM25 — proper corpus IDF (Robertson & Zaragoza)
   IDF built from all loaded docs

3. BLT — per-patch entropy, independent steps (2412.09871)
   Each 8-byte patch gets its own step count

4. SOFTMAX HOP WEIGHTING
   w_i = exp(score_i) / Σ exp(score_j)

5. GATED UNDERSTANDING UPDATE
   h_t = h_{t-1} + β * delta

6. BAYESIAN POSTERIOR
   P(pref|turns) ∝ Π P(q_t|pref) with Laplace smoothing
"""

import re
import math
import random
from pathlib import Path
from collections import Counter
from typing import List, Dict, Tuple

# Constants from bapxdi_v3
ALIGN = 8
STEPS = 64
ENTROPY_THRESH = 0.30
BM25_K1 = 1.5
BM25_B = 0.75
GATE_BETA = 0.3

# IDF cache (built at load time from corpus)
_IDF_CACHE: Dict = {}


# ============================================================================
# MATH 1: BIT DIFFUSION — Angular Encoding
# ============================================================================

def _cosine_alpha(t: float) -> float:
    """Cosine noise schedule: α_t = cos²(π/2 · (t+s)/(1+s)), s=0.008"""
    if t <= 0.0:
        return 1.0
    if t >= 1.0:
        return 0.0
    s = 0.008
    return math.cos(math.pi / 2 * (t + s) / (1.0 + s)) ** 2


def _byte_to_angle(b: int) -> float:
    """Byte b ∈ {0..255} → angle θ = 2πb/256 on unit circle"""
    return 2.0 * math.pi * b / 256.0


def _angle_to_byte(theta: float) -> int:
    """Decode: b = round(θ/(2π) · 256) mod 256"""
    b = round((theta % (2.0 * math.pi)) / (2.0 * math.pi) * 256)
    return max(0, min(255, b))


def _patch_entropy(data: bytes) -> float:
    """Shannon entropy H = -Σ p(b)log₂p(b), normalized to [0,1] by /8"""
    if not data:
        return 0.0
    c = Counter(data)
    n = len(data)
    return -sum((v / n) * math.log2(v / n) for v in c.values() if v > 0) / 8.0


def diffuse_block(signal_words: list, steps: int = STEPS) -> list:
    """
    Bit diffusion with angular encoding, cosine schedule, per-patch BLT steps.
    Each word is one patch (padded to ALIGN bytes).
    Steps allocated per patch based on patch entropy.
    """
    # Pad signals to ALIGN bytes
    signals = []
    for w in signal_words:
        raw = w.encode('utf-8')
        pad = (ALIGN - len(raw) % ALIGN) % ALIGN
        signals.append(raw + b'\x00' * pad)

    result = []
    for sig in signals:
        # BLT: per-patch entropy → per-patch steps
        h = _patch_entropy(sig)
        ps = max(8, min(steps, round(steps * (0.5 + h))))

        # Angular encoding of signal bytes
        target_angles = [_byte_to_angle(b) for b in sig]
        # Start from random angles (noise)
        thetas = [random.uniform(0, 2 * math.pi) for _ in sig]

        # Reverse diffusion
        for step in range(ps, 0, -1):
            t = step / ps
            t1 = (step - 1) / ps
            at = _cosine_alpha(t)
            at1 = _cosine_alpha(t1)
            da = at1 - at
            for i in range(len(thetas)):
                # Angular difference with wraparound
                diff = target_angles[i] - thetas[i]
                diff = (diff + math.pi) % (2 * math.pi) - math.pi
                thetas[i] = thetas[i] + da / max(1.0 - at, 1e-4) * diff

        # Decode bytes from angles
        decoded_bytes = bytes(_angle_to_byte(th) for th in thetas)
        decoded = decoded_bytes.replace(b'\x00', b'').decode('utf-8', errors='ignore').strip()
        word_i = signal_words[len(result)] if len(result) < len(signal_words) else ''
        result.append(decoded if decoded and len(decoded) >= 2 else word_i)

    return result


def byte_entropy(data: bytes) -> float:
    """Calculate byte-level entropy"""
    return _patch_entropy(data)


def diffuse_bytes_direct(signal_bytes: bytes, steps: int = STEPS) -> bytes:
    """Direct byte diffusion (non-language modalities) with angular encoding."""
    n = len(signal_bytes)
    pad = (ALIGN - n % ALIGN) % ALIGN
    sig = signal_bytes + b'\x00' * pad
    thetas = [random.uniform(0, 2 * math.pi) for _ in sig]
    targets = [_byte_to_angle(b) for b in sig]
    for step in range(steps, 0, -1):
        t = step / steps
        t1 = (step - 1) / steps
        at = _cosine_alpha(t)
        at1 = _cosine_alpha(t1)
        da = at1 - at
        for i in range(len(thetas)):
            diff = targets[i] - thetas[i]
            diff = (diff + math.pi) % (2 * math.pi) - math.pi
            thetas[i] = thetas[i] + da / max(1 - at, 1e-4) * diff
    return bytes(_angle_to_byte(th) for th in thetas)[:n]


# ============================================================================
# MATH 2: BM25 WITH PROPER CORPUS IDF
# ============================================================================

def build_corpus_idf(all_shards: list) -> dict:
    """
    Build IDF table + avg_dl from entire corpus.
    df(term) = number of documents containing term.
    N = total document count.
    avg_dl = mean document length (for BM25 length normalization).
    """
    N = max(len(all_shards), 1)
    df = Counter()
    dls = []
    for _, raw in all_shards:
        try:
            words = clean(raw.decode('utf-8', errors='ignore'))
            dls.append(len(words))
            doc_words = set(words)
            for w in doc_words:
                df[w] += 1
        except:
            pass
    avg_dl = sum(dls) / max(len(dls), 1)
    idf = {'__avg_dl__': avg_dl}
    for term, freq in df.items():
        idf[term] = math.log((N - freq + 0.5) / (freq + 0.5) + 1)
    idf['__unseen__'] = math.log((N + 0.5) / 1.5 + 1)
    return idf


def bm25_score(doc_words: list, query_words: list, avg_dl: float = 50.0) -> float:
    """
    BM25 with corpus IDF.
    score = Σ_q IDF(q) · tf(q,D)·(k1+1) / (tf(q,D) + k1·(1-b+b·|D|/avgdl))
    """
    if not doc_words or not query_words:
        return 0.0
    dl = len(doc_words)
    tf = Counter(doc_words)
    score = 0.0
    for q in query_words:
        idf = _IDF_CACHE.get(q, _IDF_CACHE.get('__unseen__', 1.0))
        term_freq = tf.get(q, 0)
        num = term_freq * (BM25_K1 + 1)
        denom = term_freq + BM25_K1 * (1 - BM25_B + BM25_B * dl / avg_dl)
        score += idf * num / max(denom, 1)
    return score


def clean(text: str) -> list:
    """Clean text and extract tokens"""
    text = re.sub(r'https?://\S+', ' ', text)
    text = re.sub(r'[|`→←⚠✓✗"\'\\]', ' ', text)
    tokens = []
    for w in text.split():
        alpha = re.sub(r'[^a-zA-Z]', '', w).lower()
        if len(alpha) >= 3:
            tokens.append(alpha)
        digits = re.sub(r'[^0-9]', '', w)
        if len(digits) >= 1:
            tokens.append(digits)
        if '_' in w:
            ident = re.sub(r'[^a-zA-Z0-9_]', '', w).lower()
            if len(ident) >= 3:
                tokens.append(ident)
    return list(dict.fromkeys(tokens))


# ============================================================================
# MATH 3: RLM PEEK (Recursive Document Windows)
# ============================================================================

def find_window(words: list, query_words: list, size: int = 20) -> tuple:
    """Find best matching window of words"""
    if len(words) < size:
        return words[:size], bm25_score(words, query_words)
    best_score, best_start = -1.0, 0
    for i in range(0, len(words) - size, size // 2):
        window = words[i:i + size]
        s = bm25_score(window, query_words)
        if s > best_score:
            best_score, best_start = s, i
    return words[best_start:best_start + size], best_score


def rlm_peek(query: str, all_shards: list, understanding: list, n: int) -> tuple:
    """
    RLM-style recursive peek at document windows.
    Returns best matching words, source doc, and score.
    """
    q_words = clean(query) + (understanding[:10] if understanding else [])
    best_s, best_w, best_doc = -1.0, [], ""
    for name, raw in all_shards:
        words = clean(raw.decode('utf-8', errors='ignore'))
        w, s = find_window(words, q_words, size=n * 2)
        if s > best_s:
            best_s, best_w, best_doc = s, w[:n], name
    return best_w, best_doc, best_s


# ============================================================================
# MATH 4: GATED UNDERSTANDING UPDATE
# ============================================================================

def gated_update(prev: list, new_signal: list, beta: float = GATE_BETA) -> list:
    """
    Scalar gate on word-level understanding update.
    h_t = h_{t-1} + beta * (new_signal - h_{t-1})
    Keeps memory bounded (finite-state principle).
    """
    prev_set = set(prev)
    delta = [w for w in new_signal if w not in prev_set]
    n_add = max(1, round(beta * len(delta)))
    updated = prev + delta[:n_add]
    return updated[-30:]  # bounded memory


# ============================================================================
# MATH 5: SOFTMAX HOP WEIGHTING
# ============================================================================

def softmax_hop_blend(hop_results: list) -> list:
    """
    Softmax weighting of hop outputs by BM25 relevance score.
    w_i = exp(s_i) / Σ exp(s_j)
    Word weight = sum of softmax weights of hops containing that word.
    """
    if not hop_results:
        return []
    scores = [s for _, s in hop_results]
    max_s = max(scores) if scores else 0.0
    exps = [math.exp(s - max_s) for s in scores]
    total = sum(exps) or 1.0
    weights = [e / total for e in exps]

    word_weight = {}
    for (words, _), w in zip(hop_results, weights):
        for word in words:
            word_weight[word] = word_weight.get(word, 0.0) + w
    return [w for w, _ in sorted(word_weight.items(), key=lambda x: x[1], reverse=True)]


# ============================================================================
# MATH 6: BAYESIAN POSTERIOR
# ============================================================================

def bayesian_posterior(turns: list) -> dict:
    """
    P(pref|turns) ∝ Π_t P(q_t|pref) · P(pref)
    Log form: log P(pref|D) = Σ_t log P(q_t|pref) + log P(pref)
    Laplace smoothing: P(q|pref) = (count(q,pref)+1)/(N+|vocab|)
    """
    if not turns:
        return {"text": 1.0}
    counts = Counter(t.get("modality", "text") for t in turns)
    N = len(turns)
    M = 12  # Number of modalities
    log_post = {}
    for mod in range(M):
        c = counts.get(mod, 0)
        likelihood = (c + 1) / (N + M)
        log_post[mod] = math.log(likelihood)
    max_lp = max(log_post.values())
    exps = {m: math.exp(v - max_lp) for m, v in log_post.items()}
    total = sum(exps.values())
    return {m: v / total for m, v in exps.items()}


# ============================================================================
# FULL GENERATION PIPELINE
# ============================================================================

def crystallize(query: str, cot_shards: list, doc_shards: list, n_words: int = 35) -> tuple:
    """
    Full crystallization pipeline (based on bapxdi_v3's generate function).
    
    Returns: (output_text, metadata_dict)
    """
    all_shards = cot_shards + doc_shards

    # Build corpus IDF if not cached
    global _IDF_CACHE
    if not _IDF_CACHE:
        _IDF_CACHE = build_corpus_idf(all_shards)

    # Determine complexity (EASY/MEDIUM/HARD)
    q_words = clean(query)
    max_idf = max(_IDF_CACHE.get(w, 1.0) for w in q_words) if q_words else 1.0
    hard_thr = min(0.3, max_idf * 0.08)
    med_thr = min(0.1, max_idf * 0.025)
    if max_idf > hard_thr:
        mode, hops = "HARD", 3
    elif max_idf > med_thr:
        mode, hops = "MEDIUM", 2
    else:
        mode, hops = "EASY", 1

    # RLM hops with gated understanding
    understanding = clean(query)
    hop_results = []
    sources = []

    for _ in range(hops):
        words, src, score = rlm_peek(query, all_shards, understanding, n_words)
        hop_results.append((words, score))
        sources.append(f"{src}({score:.2f})")
        understanding = gated_update(understanding, words, beta=GATE_BETA)

    # Softmax-weighted blend across hops
    signal_words = softmax_hop_blend(hop_results)[:n_words]
    if not signal_words:
        return "no signal", {}

    # Calculate entropy and adaptive steps
    sig_ent = byte_entropy(' '.join(signal_words).encode('utf-8'))
    adaptive_steps = max(8, min(STEPS, round(STEPS * (0.5 + sig_ent))))

    # Angular bit diffusion (CRYSTALLIZATION)
    output_words = diffuse_block(signal_words, adaptive_steps)
    output = ' '.join(output_words)

    # Calculate metrics
    best_score = max((s for _, s in hop_results), default=0.0)
    hop_efficiency = round(best_score / max(hops, 1), 4)
    output_bytes = output.encode('utf-8')
    signal_bytes = ' '.join(signal_words).encode('utf-8')
    exec_signal = round(bm25_score(clean(output), clean(' '.join(signal_words))), 4)

    return output, {
        "mode": mode,
        "hops": hops,
        "sources": sources,
        "entropy": round(sig_ent, 4),
        "steps_used": adaptive_steps,
        "refetch": sig_ent < ENTROPY_THRESH,
        "hop_efficiency": hop_efficiency,
        "exec_signal": exec_signal,
    }


# ============================================================================
# LOADER
# ============================================================================

def load_doc_bytes(directory: str) -> list:
    """Load document bytes from directory"""
    p = Path(directory)
    if not p.exists():
        return []
    return [(str(f.relative_to(p)), f.read_bytes()) for f in sorted(p.rglob("*.md"))]


# ============================================================================
# MAIN (Test)
# ============================================================================

if __name__ == "__main__":
    import time

    print("bapX-v1 Crystallization — Based on bapxdi_v3")
    print("Angular diffusion | Corpus BM25 | Per-patch BLT | Softmax blend")
    print()

    # Load shards
    cot = load_doc_bytes("./cot")
    docs = load_doc_bytes("./docs")
    print(f"Docs: {len(cot + docs)} shards — building corpus IDF...")
    _IDF_CACHE = build_corpus_idf(cot + docs)
    print(f"IDF table: {len(_IDF_CACHE)} terms")
    print()

    # Test queries (same as bapxdi_v3)
    queries = [
        "what is bit diffusion bytes words",
        "write a hashlib sha256 function",
        "rlm document external environment",
        "what is your name",
        "entropy safety refetch buffer",
        "mercury parallel generation tokens",
        "derive the eigenvalue of a symmetric matrix",
        "why does bapxdi not need training weights",
    ]

    for q in queries:
        t0 = time.time()
        out, s = crystallize(q, cot, docs, n_words=25)
        ms = round((time.time() - t0) * 1000, 1)
        print(f"Q: {q}")
        print(f"   [{s.get('mode')} hops={s.get('hops')} ent={s.get('entropy')} steps={s.get('steps_used')} {ms}ms]")
        print(f"   src: {s.get('sources', [])[0] if s.get('sources') else '?'}")
        print(f"A: {out[:85]}")
        print()
