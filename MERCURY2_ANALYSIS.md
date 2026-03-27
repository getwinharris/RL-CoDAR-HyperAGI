# Mercury-2 Diffusion LLM - Complete Analysis

**Paper:** "Mercury: Ultra-Fast Language Models Based on Diffusion" by Inception Labs

---

## 1. WHAT IS MERCURY-2?

**Mercury-2** is a **diffusion-based Large Language Model (dLLM)** that:
- Uses **Transformer architecture** (same as GPT, Claude, etc.)
- Trained with **diffusion loss** (not autoregressive loss)
- Generates tokens **in parallel** (not one-by-one like GPT)
- **10x faster** than autoregressive models (1000+ tokens/sec on H100)
- Supports **chain-of-thought reasoning**

**Key Innovation:**
Instead of predicting next token (autoregressive), Mercury:
1. Starts with **random noise** (all tokens random)
2. **Iteratively refines** all tokens in parallel
3. Each iteration makes tokens **less noisy, more coherent**
4. After T iterations → clean, coherent output

---

## 2. MERCURY-2 FORMULA (EXACT FROM PAPER)

### Forward Diffusion (Noising Process)

```
q(zt | zt-1)  for t = 1, ..., T

Where:
- x = clean data (original text tokens)
- z0 = x (start with clean data)
- zt = noisy version at timestep t
- zT = pure noise (final timestep)

The forward process q progressively adds noise:
z1 = noisy(x)
z2 = noisier(z1)
...
zT = pure noise
```

### Reverse Diffusion (Denoising Process)

```
pθ(zt-1 | zt)  for t = T, ..., 1

Where:
- θ = learned model parameters (Transformer)
- pθ = learned denoising model
- Starts from zT (pure noise)
- Iteratively removes noise
- Ends at z0 = clean text

The reverse process learns to denoise:
zT-1 = denoise(zT)
zT-2 = denoise(zT-1)
...
z0 = clean text
```

### Training Loss

```
L(x) = -Et[γ(t) · Ezt∼q log pθ(x|zt)]

Where:
- t = random timestep
- γ(t) = weight for timestep t
- zt = noisy data at timestep t
- pθ(x|zt) = model predicts clean x from noisy zt

In practice:
1. Take clean text x
2. Add noise to get zt (random t)
3. Model predicts clean x from zt
4. Loss = how wrong the prediction was
5. Update model parameters θ
```

---

## 3. MERCURY-2 INFERENCE (GENERATION)

### Algorithm:

```
Input: prompt (optional), number of steps T
Output: generated text

1. Initialize: zT = random noise (all tokens random)
2. For t = T, T-1, ..., 1:
   a. Run model: pθ(zt-1 | zt, prompt)
   b. Sample: zt-1 ~ pθ(zt-1 | zt)
   c. (Optional) Replace some tokens with prompt tokens
3. Return: z0 (final clean text)
```

### Key Properties:

1. **Parallel Generation:** All tokens updated simultaneously
2. **Coarse-to-Fine:** Early steps = rough structure, later steps = fine details
3. **Prompt Conditioning:** Can condition on prefix/suffix (for code infilling)
4. **Chain-of-Thought:** Can generate reasoning steps before answer

---

## 4. WHY MERCURY-2 IS FASTER THAN AUTOREGRESSIVE

| Autoregressive (GPT) | Diffusion (Mercury-2) |
|---------------------|----------------------|
| Generate 1 token at a time | Generate ALL tokens in parallel |
| 100 tokens = 100 forward passes | 100 tokens = ~10 forward passes |
| Sequential (can't parallelize) | Parallel (full GPU utilization) |
| Slow for long outputs | Fast for long outputs |
| 100 tokens/sec | 1000+ tokens/sec |

**Speedup:** 10x faster because:
- Autoregressive: N tokens = N sequential steps
- Diffusion: N tokens = ~10 parallel steps (regardless of N)

---

## 5. WHAT MY CODE WAS DOING WRONG

### My "Diffusion" (WRONG):

```python
# This is SEARCH, not diffusion:
def reason(query):
    results = index.search(query)  # Cosine similarity search
    return results  # Just retrieved snippets
```

**Problems:**
1. ❌ NO noise addition
2. ❌ NO denoising process
3. ❌ NO iterative refinement
4. ❌ Just cosine similarity search
5. ❌ Not diffusion at all!

### What Mercury-2 Does (CORRECT):

```python
# TRUE diffusion:
def generate(prompt, steps=10):
    # 1. Start with random noise
    z_T = random_tokens()
    
    # 2. Iteratively denoise
    for t in range(steps, 0, -1):
        # Model predicts less-noisy version
        z_{t-1} = model(z_t, prompt, t)
    
    # 3. Return clean text
    return z_0
```

**Key Differences:**
| My Code | Mercury-2 |
|---------|-----------|
| Search indexed bytes | Generate from noise |
| Cosine similarity | Learned denoising model |
| One-step retrieval | Multi-step refinement |
| No noise involved | Noise is central |
| NOT diffusion | TRUE diffusion |

---

## 6. HOW TO FIX MY CODE (Make it TRUE Diffusion)

### What Needs to Change:

**Current (Search):**
```python
def reason(query):
    # Just search index
    results = index.search(query)
    return results
```

**Should Be (Diffusion):**
```python
def generate(prompt, steps=10):
    # 1. Initialize with noise
    tokens = random_bytes(len(prompt) * 10)
    
    # 2. Iteratively refine using indexed bytes as "guide"
    for step in range(steps):
        # For each token position, check which of 256 bytes
        # best matches the "denoised" version (guided by index)
        for pos in range(len(tokens)):
            # Get context (neighboring tokens)
            context = tokens[max(0,pos-5):pos+5]
            
            # Find best-fitting byte from indexed bytes
            # (this is the "denoising model" pθ)
            best_byte = find_best_fit_byte(context, index)
            
            # Update token (denoising step)
            tokens[pos] = best_byte
    
    # 3. Return refined tokens
    return tokens
```

**Key Changes:**
1. ✅ Start with RANDOM bytes (noise)
2. ✅ Iteratively REFINE (denoise)
3. ✅ Use indexed bytes as "denoising guide" (pθ)
4. ✅ Multiple refinement steps (not one-step search)
5. ✅ TRUE diffusion process

---

## 7. CHAIN-OF-THOUGHT IN MERCURY-2

Mercury-2 supports CoT prompting:

```
User: "What is 2 + 2? Think step by step."

Mercury-2 Generation (parallel, coarse-to-fine):

Step 1 (coarse): [noise] [noise] [noise] [noise] [noise] ...
Step 2: "Let" [noise] "me" [noise] "think" [noise] ...
Step 3: "Let me" "think" "step" "by" "step" ...
Step 4: "Let me think step by step. 2 + 2 = 4."

All tokens refined in PARALLEL, not sequentially!
```

**My code should do:**
1. Parse question type (what_is, how_does, why)
2. Initialize reasoning chain with noise
3. Refine chain iteratively (diffusion)
4. Each step makes reasoning more coherent
5. Final output = refined reasoning + answer

---

## 8. SUMMARY: MERCURY-2 VS MY CODE

| Aspect | Mercury-2 | My Code (Before) | My Code (Should Be) |
|--------|-----------|------------------|---------------------|
| **Generation** | From noise | From search | From noise |
| **Process** | Iterative denoising | One-step retrieval | Iterative refinement |
| **Parallel** | Yes (all tokens) | N/A | Yes (all bytes) |
| **Speed** | 1000+ tok/sec | Fast (search) | Fast (parallel) |
| **CoT** | Supported | Not really | Should support |
| **Training** | Learned model | N/A | Indexed bytes as guide |
| **Noise** | Central concept | Not used | Central concept |

---

## 9. ACTION PLAN

1. **Remove fake "diffusion"** (cosine similarity search)
2. **Implement TRUE diffusion:**
   - Start with random bytes
   - Iteratively refine using indexed bytes as guide
   - Multiple refinement steps
3. **Add CoT support:**
   - Parse question type
   - Generate reasoning chain via diffusion
   - Crystallize answer from chain
4. **Test with real queries**

---

**Mercury-2 is TRUE diffusion. My code was just search. Need to fix this.**
