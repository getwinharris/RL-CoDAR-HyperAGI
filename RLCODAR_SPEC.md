# RLCoDAR-HyperAGI Specification

**Version:** 1.0.0  
**Date:** March 27, 2026  
**Status:** ✅ API Server Complete

---

## 🎯 Overview

**RLCoDAR-HyperAGI** = HyperAgents + RLM via OpenAI-compatible API

- **HyperAgents**: Self-improving agent system (Meta AI)
- **RLM**: Recursive Language Model with repo-as-context (MIT)
- **RLCoDAR API**: OpenAI-compatible bridge between them

---

## 🔑 API Key

**Master Key:** `rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398`

**Format:** `rlcodar-{64 hex chars}`

**Usage:** `Authorization: Bearer <key>`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│  HyperAgents (Meta AI)                                  │
│  - Meta-Agent (self-improvement)                       │
│  - Task-Agent (evaluation)                              │
│  - Uses litellm for LLM calls                          │
└────────────────────┬────────────────────────────────────┘
                     │ litellm.completion()
                     ▼
┌─────────────────────────────────────────────────────────┐
│  RLCoDAR API Server (localhost:8000)                    │
│  - OpenAI-compatible endpoint                          │
│  - API key validation                                   │
│  - Request routing                                      │
└────────────────────┬────────────────────────────────────┘
                     │ POST /v1/chat/completions
                     ▼
┌─────────────────────────────────────────────────────────┐
│  RLM (Recursive Language Model)                         │
│  - Loads repo files as context_0, context_1...         │
│  - Recursive reasoning (max_depth=2)                   │
│  - Auto-compaction when context grows                  │
│  - Code execution in REPL                              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Repository as Model Weights                            │
│  - ./rlm/ (41 Python files)                            │
│  - ./hyperagents/ (100+ files)                         │
│  - Total: ~635,536 bytes                               │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 File Structure

```
RecursiveLM/
├── rlm/                              # RLM core
│   ├── core/
│   │   ├── rlm.py                   # Main RLM class
│   │   ├── lm_handler.py            # LLM routing
│   │   └── types.py                 # Type definitions
│   ├── environments/
│   │   ├── local_repl.py            # Local REPL execution
│   │   ├── docker_repl.py           # Docker isolation
│   │   └── base_env.py              # Base environment
│   ├── clients/
│   │   ├── openai.py                # OpenAI client
│   │   ├── anthropic.py             # Anthropic client
│   │   └── ...                      # Other providers
│   └── datasets/
│       └── stream_datasets.py       # HF dataset streaming
│
├── hyperagents/                      # HyperAgents (Meta AI)
│   ├── agent/
│   │   ├── base_agent.py            # Agent base class
│   │   ├── llm.py                   # LLM via litellm
│   │   └── llm_withtools.py         # Tool-augmented LLM
│   ├── meta_agent.py                # Self-improvement agent
│   ├── task_agent.py                # Task evaluation agent
│   ├── generate_loop.py             # Main generation loop
│   └── domains/                     # Benchmark domains
│       ├── polyglot/                # Code generation
│       ├── balrog/                  # Game environments
│       └── ...
│
├── rlcodar_hyperagi/                 # RLCoDAR API (NEW)
│   ├── __init__.py                  # Package init
│   ├── api.py                       # FastAPI server
│   ├── api_key.py                   # API key management
│   └── README.md                    # Setup guide
│
├── docs/                             # Documentation
│   ├── architecture.md              # System architecture
│   ├── getting-started.md           # Quick start
│   └── api/
│       └── rlm.md                   # RLM API docs
│
└── tests/                            # Test suite
```

---

## 🔌 API Endpoints

### Health Check
```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "rlcodar-hyperagi",
  "rlm_loaded": true
}
```

---

### List Models (OpenAI Compatibility)
```
GET /v1/models
```

**Response:**
```json
{
  "object": "list",
  "data": [
    {
      "id": "rlcodar",
      "object": "model",
      "created": 1711500000,
      "owned_by": "rlcodar-hyperagi"
    }
  ]
}
```

---

### Chat Completion (Main Endpoint)
```
POST /v1/chat/completions
Authorization: Bearer rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
```

**Request:**
```json
{
  "model": "rlcodar",
  "messages": [
    {"role": "user", "content": "What is RLM?"}
  ],
  "temperature": 0.7,
  "max_tokens": 16384
}
```

**Response:**
```json
{
  "id": "rlcodar-123456",
  "object": "chat.completion",
  "created": 1711500000,
  "model": "rlcodar",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "RLM is a Recursive Language Model..."
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 50,
    "total_tokens": 60
  }
}
```

---

### RLM Status
```
GET /v1/rlm/status
```

**Response:**
```json
{
  "status": "ready",
  "backend": "openai",
  "environment": "local",
  "max_iterations": 30,
  "max_depth": 2,
  "persistent": true,
  "compaction": true
}
```

---

### Load Context
```
POST /v1/rlm/load_context
Authorization: Bearer <key>
```

**Request:**
```json
{
  "files": [
    "./rlm/core/rlm.py",
    "./hyperagents/meta_agent.py"
  ]
}
```

**Response:**
```json
{
  "loaded": [
    {
      "path": "./rlm/core/rlm.py",
      "size": 39595,
      "status": "loaded"
    },
    {
      "path": "./hyperagents/meta_agent.py",
      "size": 844,
      "status": "loaded"
    }
  ]
}
```

---

## 🚀 Usage

### Start API Server

```bash
cd /Users/getwinharris/Dev/CLI/RecursiveLM
export RLCODAR_API_KEY=rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
uv run python -m rlcodar_hyperagi.api --port 8000
```

### Configure HyperAgents

Create `hyperagents/.env`:
```bash
OPENAI_BASE_URL=http://localhost:8000/v1
OPENAI_API_KEY=rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
```

### Run HyperAgents

```bash
cd hyperagents
python generate_loop.py --domains polyglot
```

**litellm will automatically call RLCoDAR API instead of OpenAI!**

---

## 📊 Current State

### ✅ Complete

| Component | Status | Location |
|-----------|--------|----------|
| **API Server** | ✅ Working | `rlcodar_hyperagi/api.py` |
| **API Key System** | ✅ Working | `rlcodar_hyperagi/api_key.py` |
| **OpenAI Compatibility** | ✅ Working | `/v1/chat/completions` |
| **RLM Integration** | ✅ Working | RLM.completion() |
| **Health Endpoint** | ✅ Working | `/health` |
| **Models Endpoint** | ✅ Working | `/v1/models` |
| **Status Endpoint** | ✅ Working | `/v1/rlm/status` |

### ⚠️ Needs Testing

| Component | Status | Notes |
|-----------|--------|-------|
| **HyperAgents Integration** | ⚠️ Not tested | Needs litellm config |
| **Context Loading** | ⚠️ Not tested | `/v1/rlm/load_context` |
| **Recursive Reasoning** | ⚠️ Not tested | max_depth=2 |
| **Compaction** | ⚠️ Not tested | Auto-summarization |

### ❌ Not Implemented

| Component | Status | Future Work |
|-----------|--------|-------------|
| **Per-User API Keys** | ❌ Not done | Single master key only |
| **Usage Tracking** | ❌ Not done | Add to api_key.py |
| **Rate Limiting** | ❌ Not done | Add to api.py |
| **Web UI (bapx.in)** | ❌ Not done | Chat interface |
| **CoDAR Diffusion** | ❌ Not done | Byte-level generation |

---

## 🔧 Configuration

### Environment Variables

```bash
# API Server
RLCODAR_API_KEY=rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
OPENAI_API_KEY=not-needed
RLM_BACKEND=openai
RLM_MODEL=gpt-4o
PORT=8000
HOST=0.0.0.0
```

### RLM Settings

```python
RLM(
    backend="openai",       # LLM backend
    max_depth=2,            # Recursive reasoning depth
    max_iterations=30,      # Max iterations per query
    persistent=True,        # Keep context across calls
    compaction=True,        # Auto-summarize when context grows
)
```

---

## 📈 Next Steps

1. **Test with HyperAgents** - Run `generate_loop.py` with RLCoDAR API
2. **Add Web UI** - Build bapx.in chat interface
3. **Implement CoDAR** - Byte-level diffusion for generation
4. **Add Rate Limiting** - Prevent API abuse
5. **Per-User Keys** - Generate unique keys per user

---

**RLCoDAR-HyperAGI: HyperAgents with RLM reasoning via OpenAI-compatible API.**

**API Key:** `rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398`
