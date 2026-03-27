# RecursiveLM Monorepo

**Recursive Language Models + HyperAgents = Self-Improving Omni-Model**

## 📁 Monorepo Structure

```
RecursiveLM/
│
├── rlm/                          # Core RLM Python Package
│   ├── __init__.py               # Main exports (RLM, SelfImprovingRLM, etc.)
│   ├── core/                     # Core RLM engine
│   │   ├── rlm.py                # Main RLM class
│   │   ├── lm_handler.py         # LLM request routing
│   │   ├── types.py              # Type definitions
│   │   └── comms_utils.py        # Communication utilities
│   ├── agents/                   # Agent systems
│   │   └── hyper/                # HyperAgents integration
│   │       ├── meta_agent.py     # Code modification agent
│   │       └── task_agent.py     # Task solving agent
│   ├── clients/                  # LLM client wrappers
│   │   ├── openai.py
│   │   ├── anthropic.py
│   │   ├── gemini.py
│   │   └── ...
│   ├── datasets/                 # Dataset streaming
│   │   ├── stream_datasets.py    # Stream FineWeb, FineWiki, The-Stack
│   │   └── __init__.py
│   ├── environments/             # REPL environments
│   │   ├── local_repl.py
│   │   ├── docker_repl.py
│   │   ├── modal_repl.py
│   │   └── ...
│   ├── loops/                    # Training/improvement loops
│   │   ├── self_improve.py       # Self-improvement loop
│   │   └── __init__.py
│   ├── tokenizers/               # Tokenization
│   │   └── byte_tokenizer.py     # Byte-level (0-255) tokenizer
│   ├── logger/                   # Logging utilities
│   └── utils/                    # General utilities
│       └── hyper/                # HyperAgents utilities
│
├── hyperagents/                  # HyperAgents (Meta AI) - Full integration
│   ├── agent/                    # Agent implementations
│   │   ├── base_agent.py
│   │   └── llm_withtools.py
│   ├── analysis/                 # Analysis and plotting
│   ├── baselines/                # Baseline comparisons
│   ├── domains/                  # Domain-specific implementations
│   │   ├── polyglot/
│   │   ├── balrog/
│   │   └── ...
│   ├── utils/                    # HyperAgents utilities
│   │   ├── docker_utils.py
│   │   ├── gl_utils.py
│   │   └── ...
│   ├── generate_loop.py          # Main generation loop
│   ├── meta_agent.py             # Meta-agent implementation
│   ├── task_agent.py             # Task agent implementation
│   └── run_task_agent.py         # Task agent runner
│
├── docs/                         # Documentation (Docusaurus)
│   ├── docs/
│   │   ├── api/                  # API reference
│   │   ├── guides/               # User guides
│   │   └── tutorials/            # Tutorials
│   └── src/                      # Docs source
│
├── examples/                     # Example scripts
│   ├── basic_rlm.py
│   ├── dataset_streaming.py
│   └── self_improvement.py
│
├── tests/                        # Test suite
│   ├── clients/                  # Client tests
│   ├── repl/                     # REPL tests
│   └── ...
│
├── visualizer/                   # Trajectory visualizer (React)
│   ├── src/
│   └── public/
│
├── pyproject.toml                # Python project config
├── uv.lock                       # UV lockfile
├── Makefile                      # Common commands
└── README.md                     # This file
```

## 🎯 What Each Directory Does

### `rlm/` - Core RLM Package
The main Recursive Language Models implementation:
- **Infinite context** through REPL offloading
- **Auto-compaction** for long conversations
- **Persistent memory** across calls
- **Multi-provider** LLM support (OpenAI, Anthropic, Gemini, etc.)

### `hyperagents/` - HyperAgents Integration
Full Meta AI HyperAgents codebase:
- **Meta-Agent**: Automatically modifies codebase
- **Task-Agent**: Solves specific tasks
- **Evaluation loop**: Docker-based scoring
- **Archive management**: Track improvements over generations

### `rlm/datasets/` - Dataset Streaming
Stream massive datasets without downloading:
- **FineWeb**: 15T tokens of web data
- **FineWiki**: Wikipedia articles
- **The-Stack**: Code from GitHub

### `rlm/loops/` - Self-Improvement Loops
Combine RLM + HyperAgents for continuous improvement:
1. Stream dataset to REPL
2. RLM analyzes with infinite context
3. Meta-Agent generates code patches
4. Task-Agent evaluates patches
5. Apply best patches
6. Repeat → Self-improving model

### `rlm/tokenizers/` - Byte-Level Tokenization
Fixed 256-byte vocabulary (0-255):
- No training needed
- Works for any language
- Perfect for omni-modal models

## 🚀 Quick Start

### Install
```bash
uv sync
source .venv/bin/activate
```

### Basic RLM Usage
```python
from rlm import RLM

rlm = RLM(
    backend="openai",
    backend_kwargs={"model_name": "gpt-4o"},
    persistent=True
)

response = rlm.completion("Analyze this document...")
```

### Dataset Streaming
```python
from rlm import DatasetStreamer

streamer = DatasetStreamer("fineweb", limit=100)

for doc in streamer.stream_fineweb():
    print(f"Document: {len(doc['text'])} chars")
```

### Self-Improvement Loop
```python
from rlm import SelfImprovingRLM

rlm = SelfImprovingRLM(
    backend="anthropic",
    dataset="the-stack",
    max_iterations=50
)

archive = rlm.run()
```

### Run HyperAgents Loop
```bash
cd hyperagents
python generate_loop.py --domains polyglot
```

## 📊 Key Features

| Feature | Location | Description |
|---------|----------|-------------|
| **Infinite Context** | `rlm/core/rlm.py` | REPL-based context offloading |
| **Auto-Compaction** | `rlm/core/rlm.py` | Automatic summarization |
| **Dataset Streaming** | `rlm/datasets/` | Stream without downloading |
| **Byte Tokenizer** | `rlm/tokenizers/` | Fixed 256-byte vocabulary |
| **Meta-Agent** | `rlm/agents/hyper/` | Code modification agent |
| **Task-Agent** | `rlm/agents/hyper/` | Task solving agent |
| **Evaluation Loop** | `hyperagents/` | Docker-based scoring |

## 🔬 Architecture

```
┌─────────────────────────────────────────────────────────┐
│  RecursiveLM Monorepo                                   │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  rlm/       │  │ hyperagents/ │  │  datasets/   │  │
│  │  Core RLM   │  │ Meta AI      │  │  Streaming   │  │
│  └─────────────┘  └──────────────┘  └──────────────┘  │
│         ↓                ↓                 ↓           │
│         └────────────────┴─────────────────┘           │
│                          ↓                              │
│              ┌───────────────────────┐                 │
│              │  SelfImprovingRLM     │                 │
│              │  (Combined System)    │                 │
│              └───────────────────────┘                 │
└─────────────────────────────────────────────────────────┘
```

## 📚 Documentation

- **API Reference**: `docs/docs/api/`
- **Guides**: `docs/docs/guides/`
- **Tutorials**: `docs/docs/tutorials/`
- **Integration Guide**: `HYPERAGENTS_INTEGRATION.md`

## 🧪 Testing

```bash
# Run all tests
make test

# Test dataset streaming
python -m rlm.datasets.stream_datasets

# Test self-improvement
python -m rlm.loops.self_improve --iterations 5

# Run HyperAgents eval
cd hyperagents && python generate_loop.py --domains polyglot
```

## 🎯 Monorepo Benefits

1. **Single Source of Truth**: All code in one place
2. **Easy Integration**: RLM + HyperAgents work together
3. **Shared Utilities**: Common code across packages
4. **Unified Testing**: Test entire system together
5. **Simplified Deployment**: One repo to manage

## 📈 Next Steps

1. **Test Integration**: Run self-improvement loop
2. **Evaluate**: Use HyperAgents Docker eval
3. **Scale**: Increase iterations, try datasets
4. **Document**: Add examples and tutorials

---

**Monorepo structure complete! All components in one place.** 🎉
