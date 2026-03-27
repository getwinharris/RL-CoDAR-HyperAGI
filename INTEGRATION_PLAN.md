# HyperAgents × RecursiveLM Integration Plan

## What HyperAgents Does

**HyperAgents** = Self-improving code generation loop
- Meta-Agent modifies codebase
- Task-Agent solves tasks  
- Evaluate → Select best → Iterate
- Docker-based evaluation

## What RecursiveLM Does

**RLM** = Infinite context through REPL + compaction
- Offload context to variables
- Auto-summarization
- Persistent memory

## Integration: Byte-Level Self-Improving Omni-Model

### Core Idea
Use datasets (FineWeb, FineWiki, The-Stack) as **external memory variables** → byte-level (0-255) training → self-improving loop

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  HyperAgents Loop                                           │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Meta-Agent  │→ │ Task-Agent   │→ │  Evaluate    │      │
│  │ (modifies)  │  │ (solves)     │  │  (scores)    │      │
│  └─────────────┘  └──────────────┘  └──────────────┘      │
│         ↑                                      │           │
│         └────────── Select Best ───────────────┘           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  RecursiveLM External Memory                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Datasets as Variables                                │  │
│  │  context_0 = FineWeb (parquet stream)                │  │
│  │  context_1 = FineWiki (HF dataset)                   │  │
│  │  context_2 = The-Stack (code)                        │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Byte-Level Tokenization (0-255)                     │  │
│  │  - Each byte = token                                 │  │
│  │  - No BPE/wordpiece overhead                         │  │
│  │  - Direct binary representation                      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Self-Improvement Loop                                      │
│  1. Stream dataset → REPL variable                         │
│  2. RLM analyzes → generates code patches                  │
│  3. HyperAgents evaluates patches                          │
│  4. Best patches → update model weights                    │
│  5. Repeat with new context                                │
└─────────────────────────────────────────────────────────────┘
```

## Files to Add from HyperAgents

### 1. Core Agent System
**From:** `HyperAgents/agent/`
**To:** `rlm/agents/hyper/`

- `base_agent.py` → Agent abstraction
- `llm_withtools.py` → Tool-augmented LLM
- `meta_agent.py` → Code modification agent
- `task_agent.py` → Task solving agent

### 2. Evaluation Loop
**From:** `HyperAgents/generate_loop.py`
**To:** `rlm/loops/self_improve.py`

- Docker-based evaluation
- Score computation
- Parent selection
- Archive management

### 3. Domain Evaluators
**From:** `HyperAgents/domains/`
**To:** `rlm/evals/`

- Polyglot (code generation)
- Balrog (reasoning)
- Custom evals for your tasks

### 4. Utilities
**From:** `HyperAgents/utils/`
**To:** `rlm/utils/hyper/`

- Docker utilities
- Diff/patch handling
- Archive management

## New Files to Create

### 1. Dataset Streaming Module
```python
# rlm/datasets/stream_datasets.py
from datatrove.pipeline.readers import ParquetReader
from datasets import load_dataset

class DatasetStreamer:
    def __init__(self, dataset_name, split=None):
        self.dataset_name = dataset_name
        self.split = split
        
    def stream_to_repl(self, var_name="context"):
        """Stream dataset to REPL variable without downloading"""
        if "fineweb" in self.dataset_name:
            reader = ParquetReader("hf://datasets/HuggingFaceFW/fineweb/data")
            for doc in reader():
                yield doc  # Stream to REPL
                
        elif "finewiki" in self.dataset_name:
            ds = load_dataset(self.dataset_name, split=self.split)
            for item in ds:
                yield item
                
        elif "the-stack" in self.dataset_name:
            ds = load_dataset(self.dataset_name)
            for file in ds:
                yield file
```

### 2. Byte-Level Tokenizer
```python
# rlm/tokenizers/byte_tokenizer.py
class ByteTokenizer:
    """Byte-level tokenizer (0-255) for omni-model"""
    
    def encode(self, text: str) -> list[int]:
        """Convert text to byte sequence"""
        return [b for b in text.encode('utf-8')]
    
    def decode(self, bytes: list[int]) -> str:
        """Convert byte sequence to text"""
        return bytes(bytes).decode('utf-8')
    
    def train_from_stream(self, dataset_stream, vocab_size=256):
        """No training needed - fixed 256 byte vocabulary"""
        # Byte-level models don't need vocab training
        return {"vocab_size": 256, "type": "byte"}
```

### 3. Self-Improvement Loop
```python
# rlm/loops/self_improve.py
from rlm import RLM
from rlm.datasets import DatasetStreamer
from rlm.agents.hyper import MetaAgent, TaskAgent

class SelfImprovingRLM:
    def __init__(self, backend, dataset_name):
        self.rlm = RLM(backend=backend, persistent=True)
        self.dataset = DatasetStreamer(dataset_name)
        self.meta_agent = MetaAgent()
        self.task_agent = TaskAgent()
        
    def improve_step(self):
        """One step of self-improvement"""
        # 1. Stream new context
        context = next(self.dataset.stream_to_repl())
        
        # 2. RLM analyzes with infinite context
        analysis = self.rlm.completion(f"Analyze: {context}")
        
        # 3. Meta-agent generates code patches
        patches = self.meta_agent.forward(
            repo_path="./codebase",
            analysis=analysis
        )
        
        # 4. Task-agent evaluates patches
        scores = self.task_agent.forward(patches)
        
        # 5. Apply best patches
        best_patch = max(patches, key=lambda p: scores[p])
        apply_patch(best_patch)
        
        return scores, best_patch
```

## Integration Steps

### Phase 1: Copy HyperAgents Core (Week 1)
1. Copy `agent/` → `rlm/agents/hyper/`
2. Copy `utils/` → `rlm/utils/hyper/`
3. Adapt to RLM's existing agent system

### Phase 2: Dataset Integration (Week 2)
1. Create `rlm/datasets/` module
2. Implement streaming from FineWeb/FineWiki/The-Stack
3. Load as REPL variables (not downloading)

### Phase 3: Byte-Level Tokenization (Week 3)
1. Create `rlm/tokenizers/byte_tokenizer.py`
2. Integrate with RLM's existing token utils
3. Test byte-level (0-255) encoding

### Phase 4: Self-Improvement Loop (Week 4)
1. Combine HyperAgents loop with RLM compaction
2. Docker-based evaluation
3. Automatic patch application

## Key Differences from Traditional Training

| Traditional Training | RLM + HyperAgents |
|---------------------|-------------------|
| Download full dataset | Stream to REPL variables |
| Fixed training set | Dynamic, evolving context |
| Batch gradient descent | Code patches via Meta-Agent |
| Expensive GPU hours | Cheap API calls |
| Static weights | Continuously improving |

## Expected Benefits

1. **No Download Needed**: Datasets stream to REPL
2. **Byte-Level Efficiency**: 0-255 vocabulary, no BPE
3. **Self-Improving**: Code patches update behavior
4. **Infinite Context**: RLM compaction handles any size
5. **Continuous Learning**: Evolves with each iteration

## Next Steps

1. **Clone HyperAgents code** into `rlm/`
2. **Create dataset streaming** module
3. **Implement byte tokenizer**
4. **Build self-improvement loop**
5. **Test with FineWeb sample**
