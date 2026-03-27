# VL-JEPA — What bapXdi Learns
hf.co/papers/2512.10942
Authors: Delong Chen, Mustafa Shukor, Yann LeCun et al. December 2025.

WHAT VL-JEPA DOES:
Instead of predicting next TOKEN (autoregressive), predicts TARGET EMBEDDING.
Loss: alignment between predicted embedding Ŝ_y and actual target embedding S_y.
Works in abstract representation space — not token space.
Result: 50% fewer parameters, stronger performance.
Selective decoding: Y-Decoder only invoked when needed → 2.85x fewer decode ops.
One architecture: generation, retrieval, classification, VQA — all without modification.

THE CORE JEPA INSIGHT:
Token-space prediction forces model to recreate exact surface form.
Embedding-space prediction forces model to capture SEMANTICS.
The model focuses on what something MEANS, not how it is spelled.

FOR BAPXDI — BYTE SPACE IS EMBEDDING SPACE:
VL-JEPA avoids token space by predicting embeddings.
bapXdi has no token space at all. Word bytes ARE the embedding.
"diffusion".encode('utf-8') = [100,105,102,102,117,115,105,111,110]
Those bytes ARE the abstract representation.
No encoder needed. The bytes ARE the embedding.
bapXdi already operates in what VL-JEPA is trying to reach.

WHAT TO TAKE FROM VL-JEPA WITHOUT TRAINING:

1. SELECTIVE DECODING → already implemented as BLT entropy
   VL-JEPA: skip Y-Decoder when prediction is confident
   bapXdi: skip diffusion steps when entropy < threshold
   Same principle. Already in v3.0.

2. X/Y ENCODER SEPARATION = language routing + document bytes
   VL-JEPA: X-Encoder processes vision, Y-Encoder processes text target
   bapXdi: language_route() = X-Encoder (finds the right modality)
           Document bytes = Y-Encoder (the target representation)
   No learned encoder. BM25 routing IS the X-Encoder.
   HF dataset bytes ARE the Y-Encoder output.

3. UNIFIED ARCHITECTURE across tasks
   VL-JEPA: same model for generation, retrieval, classification
   bapXdi: same diffuse_block() for text, image, audio, code
   Already implemented.

4. PREDICTOR = RLM
   VL-JEPA: Predictor (Llama 3 layers) bridges X and Y spaces
   bapXdi: RLM hops bridge query understanding and document bytes
   The predictor's job = find the relevant bytes = RLM's job.

TTT CONNECTION (Test-Time Training):
VL-JEPA trains once, deploys.
TTT: update model AT test time without full retraining.
bapXdi: writing to docs/ IS TTT. Each query that improves a doc = one TTT step.
Bayesian posterior update = TTT in document space.
No gradient. No backward pass. Document write = weight update.

KARPATHY V-JEPA / AUTOREGRESSIVE CONNECTION:
V-JEPA (Karpathy-era LeCun work): predict masked patches in embedding space.
bapXdi: predict masked byte positions via diffusion.
Both avoid token-by-token autoregression.
Both work in representation space.
bapXdi: representation = bytes (hardware native).
V-JEPA: representation = learned embeddings.
bytes > learned embeddings for portability.
