# bapX-v1

**Recursive Language Continuous Diffusion with Contextual AutoRegressive Decoder**

---

## 🎯 Overview

**bapX-v1** is a pure Python diffusion model that operates directly on bytes (0-255) from your local files.

**NO external APIs. NO numpy. NO torch. NO training.**

**RLCoDAR** is the mechanism:
- **RL** = **R**ecursive **L**anguage (from RLM - files as context/weights)
- **CoDAR** = **Co**ntinuous **D**iffusion with Contextual **A**uto**R**egressive **D**ecoder

---

## 🏗️ Architecture

```
bapX-v1 (Model)
    │
    └── Uses RLCoDAR (Mechanism)
            │
            ├── RL (from RLM)
            │   ├── load_context() - Load files as weights
            │   ├── REPL environment - Execute code
            │   └── Byte indexing - Index bytes from repo files
            │
            └── CoDAR
                ├── ByteIndex - Searchable byte index
                ├── CosineNoiseSchedule - Diffusion noise schedule
                ├── Diffusion Process - Forward/reverse diffusion
                └── AR Decoder - Contextual byte generation
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Only HuggingFace datasets needed for streaming
pip install datasets
```

### 2. Use bapX-v1

```python
from rlcodar_hyperagi.diffusion import CoDARDiffusion, ByteIndex

# Create byte index (the model's "weights")
byte_index = ByteIndex()

# Index your files
byte_index.add_text("doc1", "Python is a programming language")
byte_index.add_text("doc2", "CoDAR is a diffusion model")

# Or index entire directories
import os
for root, dirs, files in os.walk('./my-project'):
    for f in files:
        if f.endswith('.py'):
            with open(os.path.join(root, f)) as file:
                byte_index.add_text(f, file.read())

# Create bapX-v1 model
bapx = CoDARDiffusion(byte_index=byte_index)

# Query the model (NO API KEY NEEDED!)
response = bapx.reason("What is Python?")
print(response)
```

---

## 📊 How It Works

### 1. **RL - Recursive Language (from RLM)**

```python
# RLM provides file loading mechanism
from rlm import RLM

rlm = RLM(environment='local', persistent=True)

# Load files as context (these become the "weights")
with open('my_code.py') as f:
    rlm._persistent_env.load_context({"code": f.read()})

# Now the model can query these files
```

### 2. **CoDAR - Continuous Diffusion with AR Decoder**

```python
# CoDAR provides diffusion
from rlcodar_hyperagi.diffusion import CoDARDiffusion, ByteIndex, CosineNoiseSchedule

# Create byte index
byte_index = ByteIndex()
byte_index.add_text("file.py", open("file.py").read())

# Create diffusion model
schedule = CosineNoiseSchedule(T=1000)
codar = CoDARDiffusion(byte_index=byte_index, schedule=schedule)

# Query
response = codar.reason("What does file.py do?")
```

### 3. **RLCoDAR Integration**

```python
# RLCoDAR = RL + CoDAR
from rlcodar_hyperagi.diffusion import CoDARDiffusion, ByteIndex

# RL part: Load files
byte_index = ByteIndex()
for filepath in ['./src', './docs']:
    # ... load files ...
    byte_index.add_text(filepath, content)

# CoDAR part: Diffusion
bapx_v1 = CoDARDiffusion(byte_index=byte_index)

# Query your own files (NO external API!)
response = bapx_v1.reason("Explain my code")
```

---

## 🔬 Technical Details

### Byte-Level Tokenization

```python
# "Hello World!" → Byte groups
[[72, 101, 108, 108, 111],    # "Hello"
 [32],                         # " "
 [87, 111, 114, 108, 100, 33]] # "World!"
```

### Diffusion Process

```python
# Forward diffusion (add noise)
q(x_t | x_0) = N(x_t; sqrt(α_t) * x_0, (1 - α_t) * I)

# Reverse diffusion (denoise)
x_{t-1} = x_t - η * v_θ(x_t, t)

# Where v_θ is predicted by the model
```

### AR Decoder

```python
# Contextual rounding from continuous to discrete bytes
P(a_t | State) = AR_Decoder(cross_attention(x_0, W_rules))
```

---

## 📁 File Structure

```
RecursiveLM/
├── rlm/                           # RLM (provides RL part)
│   ├── core/
│   │   └── rlm.py                # RLM class with load_context()
│   ├── environments/
│   │   └── local_repl.py         # REPL environment
│   └── datasets/
│       └── stream_datasets.py    # Dataset streaming
│
├── rlcodar_hyperagi/              # RLCoDAR integration
│   └── diffusion.py              # CoDAR implementation
│       ├── ByteIndex             # Byte indexing
│       ├── CosineNoiseSchedule   # Noise schedule
│       ├── CoDARDiffusion        # Main diffusion class
│       └── ByteGroupTokenizer    # Byte tokenization
│
└── hyperagents/                   # HyperAgents (self-improvement)
    ├── meta_agent.py             # Meta-agent for code modification
    └── task_agent.py             # Task evaluation
```

---

## 🧪 Testing

### Test bapX-v1

```python
from rlcodar_hyperagi.diffusion import CoDARDiffusion, ByteIndex

# Create model
byte_index = ByteIndex()
byte_index.add_text("test", "Python is a programming language")
bapx = CoDARDiffusion(byte_index=byte_index)

# Query
response = bapx.reason("What is Python?")
print(f"Response: {response}")
```

### Test RLCoDAR

```python
# Test full RLCoDAR mechanism
from rlm import RLM
from rlcodar_hyperagi.diffusion import CoDARDiffusion, ByteIndex

# RL part
rlm = RLM(environment='local', persistent=True)

# CoDAR part
byte_index = ByteIndex()
codar = CoDARDiffusion(byte_index=byte_index)

# Together = RLCoDAR
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| **Parameters** | 0 (no training, files are weights) |
| **Vocabulary** | 256 (bytes 0-255) |
| **Context Length** | Unlimited (files loaded on demand) |
| **Inference Speed** | ~100ms per query (depends on index size) |
| **Memory Usage** | ~1MB per 1000 indexed bytes |

---

## 🎯 Use Cases

### 1. **Code Understanding**

```python
# Index your codebase
byte_index = ByteIndex()
for root, dirs, files in os.walk('./my-project'):
    for f in files:
        if f.endswith('.py'):
            with open(os.path.join(root, f)) as file:
                byte_index.add_text(f, file.read())

bapx = CoDARDiffusion(byte_index=byte_index)

# Query your code
response = bapx.reason("How does authentication work?")
```

### 2. **Documentation Q&A**

```python
# Index documentation
byte_index.add_text("README.md", open("README.md").read())
byte_index.add_text("docs/api.md", open("docs/api.md").read())

bapx = CoDARDiffusion(byte_index=byte_index)

# Query docs
response = bapx.reason("What is the API for diffusion?")
```

### 3. **Dataset Q&A**

```python
# Stream and index datasets
from rlm.datasets import DatasetStreamer

streamer = DatasetStreamer("fineweb", limit=100)
for doc in streamer.stream_fineweb():
    byte_index.add_text(f"fineweb_{i}", doc['text'])

bapx = CoDARDiffusion(byte_index=byte_index)

# Query dataset
response = bapx.reason("What topics are covered?")
```

---

## 🔧 Configuration

### Diffusion Settings

```python
from rlcodar_hyperagi.diffusion import CoDARDiffusion, CosineNoiseSchedule

# Custom noise schedule
schedule = CosineNoiseSchedule(T=1000, s=0.008)

# Custom diffusion
bapx = CoDARDiffusion(
    byte_index=byte_index,
    schedule=schedule,
    steps=100  # Number of diffusion steps
)
```

### Index Settings

```python
from rlcodar_hyperagi.diffusion import ByteIndex

# Custom index
byte_index = ByteIndex(
    max_groups=10000,  # Max byte groups
    similarity_threshold=0.7  # Min similarity for results
)
```

---

## 📚 References

- **RLM Paper**: [Recursive Language Models](https://arxiv.org/abs/2512.24601)
- **CoDAR Paper**: [Continuous Diffusion with Contextual AR Decoder](https://arxiv.org/abs/2603.02547)
- **HyperAgents**: [Self-Improving Agents](https://arxiv.org/abs/2603.19461)

---

## 🤝 Contributing

1. **Add new datasets** - Stream from HuggingFace or local files
2. **Improve diffusion** - Better noise schedules, faster sampling
3. **Extend AR decoder** - Better contextual rounding
4. **Add HyperAgents integration** - Self-improvement loop

---

## 📄 License

MIT License - See LICENSE file for details.

---

**bapX-v1: Pure Python diffusion. Your files are the weights. NO external APIs.**
