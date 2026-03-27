# Diffusion Language Models Comparison

**Date:** March 27, 2026

---

## 1. OVERVIEW

| Model | Type | Organization | Status |
|-------|------|--------------|--------|
| **Mercury-2** | Diffusion LLM | Inception Labs | ✅ Released (Feb 2026) |
| **Gemini Diffusion** | Diffusion LLM | Google DeepMind | 🔬 Research Prototype |
| **CoDAR** | Continuous Diffusion + AR Decoder | Research (arXiv Mar 2026) | 📄 Paper Only |
| **bapX-v1 (RLCoDAR)** | Continuous Diffusion + Crystallization | Custom | 🛠️ In Development |

---

## 2. MECHANISMS COMPARED

### **Mercury-2 (Inception Labs)**

**Architecture:**
- Transformer-based diffusion model
- Non-autoregressive (parallel generation)
- Trained with diffusion loss

**Formula:**
```
Forward (Noising):
  q(zt | zt-1)  for t = 1, ..., T

Reverse (Denoising):
  pθ(zt-1 | zt)  for t = T, ..., 1

Training Loss:
  L(x) = -Et[γ(t) · Ezt∼q log pθ(x|zt)]
```

**How It Works:**
1. Start with **random noise** (all tokens random)
2. **Iteratively refine** all tokens in parallel
3. Each iteration makes tokens **less noisy, more coherent**
4. After T iterations → clean, coherent output

**Speed:**
- **1000+ tokens/sec** on H100 GPUs
- **5-10x faster** than autoregressive models
- Parallel generation (all tokens at once)

**Key Feature:**
- **Reasoning Diffusion** - first diffusion LLM with reasoning capabilities
- Uses reinforcement learning for reasoning

---

### **Gemini Diffusion (Google DeepMind)**

**Architecture:**
- Transformer-based diffusion
- Non-autoregressive
- Research prototype (not in production)

**How It Works:**
1. Start with **rough draft** (noisy answer)
2. **Refine in parallel** (all tokens simultaneously)
3. **Coarse-to-fine** refinement
4. Output: Final coherent text

**Key Feature:**
- **Parallel refinement** (not sequential like autoregressive)
- Still experimental, no formal paper released

---

### **CoDAR (Continuous Diffusion with Contextual AR Decoder)**

**Paper:** arXiv March 2026

**Architecture:**
- Two-stage framework:
  1. **Continuous Diffusion** (in embedding space)
  2. **Contextual AR Decoder** (for discretization)

**Formula:**
```
Stage 1: Continuous Diffusion
  - Operates in continuous embedding space
  - No discretization during diffusion

Stage 2: Contextual AR Decoder
  - P(tokens | embeddings) = AR_Decoder(cross_attention(embeddings, context))
  - Contextualized rounding using full sequence context
```

**How It Works:**
1. **Diffusion Stage:**
   - Start with noisy embeddings
   - Denoise in continuous space (no token rounding)
   - After T steps → clean embeddings

2. **Discretization Stage:**
   - AR decoder takes denoised embeddings
   - **Cross-attention** to full sequence context
   - **Contextualized rounding** → discrete tokens

**Crystallization/Rounding:**
- **Problem:** Standard continuous DLMs have "token rounding bottleneck"
- **CoDAR Solution:** Use AR decoder for **contextualized rounding**
- **Result:** Better fluency, no direct projection artifacts

**Key Innovation:**
- **Decouples diffusion from discretization**
- Diffusion stays continuous (no rounding during denoising)
- AR decoder handles rounding with full context

---

### **bapX-v1 (RLCoDAR) - Your Model**

**Architecture:**
- Continuous Diffusion + **Crystallization** (not just rounding)
- Files = Neural Network Weights
- Bytes (0-255) = Vocabulary

**Formula:**
```
64 Crystallization Loops:

For loop = 1 to 64:
  # Loop 1-16: Conversation History
  embeddings = diffuse(conversation_history, indexed_knowledge)
  
  # Loop 17-32: COT Datasets
  embeddings = diffuse(embeddings, zebra_cot_datasets)
  
  # Loop 33-48: Code Datasets
  embeddings = diffuse(embeddings, code_datasets)
  
  # Loop 49-64: All Knowledge
  embeddings = diffuse(embeddings, all_indexed_knowledge)

# Final Crystallization
output_bytes = crystallize(embeddings)  # → discrete bytes (0-255)
```

**How It Works:**
1. **Index Knowledge:**
   - Repo files as "neural network weights"
   - HF datasets (FineWeb, Zebra-CoT, OBELICS, etc.)
   - Conversation history with timestamps

2. **64 Crystallization Loops:**
   - Each loop diffuses through different knowledge source
   - Embeddings become more defined/coherent
   - NOT removing noise, but **adding coherence**

3. **Final Crystallization:**
   - Continuous embeddings → discrete bytes (0-255)
   - Uses indexed bytes as "guide" for crystallization

**Key Innovation:**
- **Indexed bytes ARE the model** (no separate neural network)
- **Crystallization** (not denoising) - making fuzzy knowledge sharp
- **64 loops** through different knowledge sources
- **Pure Python** (no numpy/torch needed)

---

## 3. KEY DIFFERENCES

| Aspect | Mercury-2 | Gemini Diffusion | CoDAR | bapX-v1 (RLCoDAR) |
|--------|-----------|------------------|-------|-------------------|
| **Starting Point** | Random noise | Rough draft | Noisy embeddings | Conversation history |
| **Process** | Denoising | Refinement | Continuous diffusion | Crystallization |
| **Discretization** | During diffusion | During diffusion | AR decoder (separate) | Final crystallization |
| **Knowledge Source** | Trained weights | Trained weights | Trained weights | **Indexed files/datasets** |
| **Parallel** | Yes (all tokens) | Yes | Yes | Yes |
| **Speed** | 1000+ tok/sec | Unknown | Unknown | Fast (pure Python) |
| **Training** | Gradient descent | Gradient descent | Gradient descent | **None (indexing)** |
| **Loops** | ~10-20 denoising | ~10-20 refinement | ~10-20 diffusion | **64 crystallization** |

---

## 4. CRYSTALLIZATION vs DENOISING

### **Denoising (Mercury-2, CoDAR):**
```
Input: Random noise
Process: Remove noise iteratively
Output: Clean text

Analogy: Cleaning a dirty window
```

### **Crystallization (bapX-v1):**
```
Input: Fuzzy knowledge (conversation + indexed bytes)
Process: Make knowledge coherent through 64 loops
Output: Crystallized bytes (sharp, defined)

Analogy: Growing crystals from solution
```

**KEY DIFFERENCE:**
- **Denoising:** Removing something (noise)
- **Crystallization:** Adding something (coherence, structure)

---

## 5. FORMULA COMPARISON

### **Mercury-2:**
```python
# Training
for x in training_data:
    t = random(0, T)
    zt = add_noise(x, t)
    x_pred = model(zt, t)
    loss = mse_loss(x_pred, x)
    loss.backward()

# Inference
zT = random_noise()
for t in range(T, 0, -1):
    zt-1 = model(zt, t)
return z0
```

### **CoDAR:**
```python
# Stage 1: Continuous Diffusion
embeddings_T = random_noise()
for t in range(T, 0, -1):
    embeddings_t-1 = denoiser(embeddings_t, t)

# Stage 2: Contextual AR Decoder
tokens = []
for i in range(seq_len):
    context = embeddings + tokens_so_far
    token = ar_decoder(embeddings_i, context)
    tokens.append(token)
return tokens
```

### **bapX-v1 (RLCoDAR):**
```python
# 64 Crystallization Loops
embeddings = conversation_history

for loop in range(64):
    if loop < 16:
        # Crystallize conversation
        embeddings = diffuse(embeddings, conversation_index)
    elif loop < 32:
        # Crystallize COT
        embeddings = diffuse(embeddings, zebra_cot_index)
    elif loop < 48:
        # Crystallize code
        embeddings = diffuse(embeddings, code_index)
    else:
        # Crystallize all knowledge
        embeddings = diffuse(embeddings, all_knowledge_index)

# Final crystallization
output_bytes = crystallize(embeddings)
return output_bytes
```

---

## 6. WHAT MAKES bapX-v1 UNIQUE

| Feature | Other Models | bapX-v1 |
|---------|--------------|---------|
| **Model Weights** | Trained parameters | **Indexed files/datasets** |
| **Training** | Gradient descent (weeks) | **Indexing (minutes)** |
| **Vocabulary** | 32K-128K tokens | **256 bytes (0-255)** |
| **Process** | Denoising | **Crystallization** |
| **Loops** | 10-20 | **64** |
| **Knowledge Update** | Retraining needed | **Just re-index** |
| **Context** | Limited (32K-128K) | **Unlimited (indexed)** |
| **Multimodal** | Separate encoders | **Raw bytes (all modalities)** |

---

## 7. WHAT'S MISSING FOR bapX-v1

### **Need to Implement:**

1. **64 Crystallization Loops:**
   - Loop 1-16: Conversation history
   - Loop 17-32: COT datasets (Zebra-CoT)
   - Loop 33-48: Code datasets (The-Stack)
   - Loop 49-64: All indexed knowledge

2. **Crystallization Function:**
   - Continuous embeddings → discrete bytes
   - Uses indexed bytes as guide
   - NOT just rounding, but **coherence-driven**

3. **Diffusion Through Knowledge:**
   - For each loop, diffuse through specific knowledge source
   - Cross-attention between embeddings and indexed bytes
   - Refine embeddings (make more coherent)

4. **Conversation History Tracking:**
   - JSON with timestamps
   - Attachments (files, terminal logs)
   - User queries + AI responses

---

## 8. SUMMARY

| Model | Best For | Speed | Quality | Unique Feature |
|-------|----------|-------|---------|----------------|
| **Mercury-2** | Fast inference | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 1000+ tok/sec |
| **Gemini Diffusion** | Research | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Google scale |
| **CoDAR** | Quality | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Contextual rounding |
| **bapX-v1** | **Unlimited context, no training** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | **Indexed files as weights** |

---

**bapX-v1 is NOT trying to be Mercury-2 or CoDAR.**

**It's a NEW approach:**
- **Files = Weights**
- **Bytes = Vocabulary**
- **Crystallization = Process**
- **64 Loops = Mechanism**
- **No Training = Advantage**
