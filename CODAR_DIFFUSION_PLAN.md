# CoDAR Diffusion Implementation Plan

## Current State
- ✅ API Server: Working
- ✅ API Key: Working
- ✅ RLM: Working (calls OpenAI)
- ❌ Diffusion: NOT IMPLEMENTED

## What CoDAR Needs (From Your Formulas)

### 1. Byte-Level Diffusion
```python
# Forward Diffusion (Adding Noise)
q(x_t | x_0) = N(x_t; sqrt(α_t) * x_0, (1 - α_t) * I)

# Where:
# - x_0: Original bytes (0-255) from repo files
# - x_t: Noisy bytes at timestep t
# - α_t: Noise schedule (cosine)
```

### 2. Velocity Prediction (CoDAR)
```python
# Predict velocity instead of noise
v_θ(x_t, t) = (ε_θ * sqrt(α_t) - x_t * sqrt(1 - α_t)) / sqrt(α_t)

# Loss function
L_velocity = E[||v - v_θ(x_t, t)||²]
```

### 3. Reverse Diffusion
```python
# Denoise from noise to bytes
x_{t-1} = x_t - η * v_θ(x_t, t) + σ_t * ∇log P(docs | x_t)
```

### 4. AR Decoder (Contextual Rounding)
```python
# Round continuous to discrete bytes (0-255)
P(a_t | State) = AR_Decoder(cross_attention(x_0, W_rules))
```

## Implementation Steps

### Step 1: Create Diffusion Module
```
rlcodar_hyperagi/
├── diffusion/
│   ├── __init__.py
│   ├── scheduler.py      # Noise schedule (cosine)
│   ├── unet.py           # U-Net for velocity prediction
│   └── sampler.py        # Reverse diffusion sampler
```

### Step 2: Byte-Level Encoding
```python
# Convert repo files to byte sequences
def files_to_bytes(file_paths):
    all_bytes = []
    for path in file_paths:
        with open(path, 'rb') as f:
            all_bytes.extend(list(f.read()))
    return np.array(all_bytes) / 255.0  # Normalize to [0, 1]
```

### Step 3: Train Velocity Predictor
```python
# Training loop
for batch in dataloader:
    x_0 = batch  # Byte sequences
    t = random.randint(0, T)
    ε = torch.randn_like(x_0)
    
    # Add noise
    x_t = sqrt(α_t) * x_0 + sqrt(1 - α_t) * ε
    
    # True velocity
    v = (ε * sqrt(α_t) - x_0 * sqrt(1 - α_t)) / sqrt(α_t)
    
    # Predict velocity
    v_pred = unet(x_t, t)
    
    # Loss
    loss = mse_loss(v_pred, v)
    loss.backward()
```

### Step 4: Generation with RLM Context
```python
def generate(prompt_bytes, rlm_context, steps=1000):
    # Start from noise
    x_T = torch.randn(1, seq_len, 256)
    
    # Reverse diffusion
    for t in reversed(range(steps)):
        # Get RLM context as guidance
        context = rlm.completion(prompt_bytes)
        
        # Predict velocity
        v = unet(x_t, t, context)
        
        # Reverse step
        x_t = reverse_step(x_t, v, t)
    
    # Round to bytes (0-255)
    x_0 = (x_t * 255).clamp(0, 255).round().int()
    
    return x_0
```

## Files to Create

1. `rlcodar_hyperagi/diffusion/__init__.py`
2. `rlcodar_hyperagi/diffusion/scheduler.py`
3. `rlcodar_hyperagi/diffusion/unet.py`
4. `rlcodar_hyperagi/diffusion/sampler.py`
5. `rlcodar_hyperagi/diffusion/train.py`
6. Update `rlcodar_hyperagi/api.py` to use diffusion

## Current Blockers

1. **No Training Data** - Need to prepare byte sequences from repo
2. **No Model Architecture** - Need U-Net for velocity prediction
3. **No Training Loop** - Need to train on repo bytes
4. **API Key Needed** - RLM currently calls OpenAI, not local diffusion

## Immediate Actions

1. Create diffusion module structure
2. Implement cosine noise schedule
3. Implement U-Net architecture
4. Create training script
5. Update API to use diffusion instead of OpenAI
