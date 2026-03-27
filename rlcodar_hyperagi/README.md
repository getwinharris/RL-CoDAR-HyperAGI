# RLCoDAR-HyperAGI Setup Guide

## Architecture

```
HyperAgents → litellm → RLCoDAR API (localhost:8000) → RLM → Repo files as context
```

**NO code changes to HyperAgents needed!**

---

## API Key

**Master API Key:** `rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398`

Use this key in Authorization header:
```bash
Authorization: Bearer rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
```

---

## Quick Start

### 1. Set Environment Variables

```bash
cd /Users/getwinharris/Dev/CLI/RecursiveLM
export RLCODAR_API_KEY=rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
```

### 2. Start RLCoDAR-HyperAGI API Server

```bash
uv run python -m rlcodar_hyperagi.api --port 8000
```

### 3. Configure HyperAgents (.env file)

```bash
# HyperAgents/.env
OPENAI_BASE_URL=http://localhost:8000/v1
OPENAI_API_KEY=rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398
```

### 3. Run HyperAgents (no changes needed!)

```bash
cd hyperagents
python generate_loop.py --domains polyglot
```

**litellm will automatically call the RLCoDAR API instead of OpenAI!**

---

## API Endpoints

### Health Check
```bash
curl http://localhost:8000/health
```

### List Models (OpenAI compatibility)
```bash
curl http://localhost:8000/v1/models
```

### Chat Completion (what litellm uses)
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello!"}]}'
```

### RLM Status
```bash
curl http://localhost:8000/v1/rlm/status
```

### Load Context (load repo files as "model weights")
```bash
curl -X POST http://localhost:8000/v1/rlm/load_context \
  -H "Content-Type: application/json" \
  -d '{"files":["./rlm/core/rlm.py","./hyperagents/meta_agent.py"]}'
```

---

## Configuration

### Environment Variables

```bash
# API Server
RLM_BACKEND=openai          # Backend to use (openai, anthropic, etc.)
RLM_MODEL=gpt-4o           # Model name
OPENAI_API_KEY=sk-...      # Your API key

# Server settings
PORT=8000                  # API server port
HOST=0.0.0.0               # Bind address
```

### RLM Settings (in api.py)

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

## How It Works

### 1. HyperAgents Makes LLM Call

```python
# hyperagents/agent/llm_withtools.py (unchanged)
from litellm import completion

response = completion(
    model="openai/gpt-4o",
    messages=[{"role": "user", "content": "Modify this code..."}]
)
```

### 2. litellm Calls RLCoDAR API

```bash
POST http://localhost:8000/v1/chat/completions
{
  "model": "openai/gpt-4o",
  "messages": [{"role": "user", "content": "Modify this code..."}]
}
```

### 3. RLCoDAR Calls RLM

```python
# rlcodar_hyperagi/api.py
result = _rlm_instance.completion("Modify this code...")
```

### 4. RLM Uses Repo as Context

```python
# rlm/environments/local_repl.py
context_0 = load_file("./rlm/core/rlm.py")
context_1 = load_file("./hyperagents/meta_agent.py")
# ... model reasons over these files
```

### 5. Response Returns to HyperAgents

```python
# Back in HyperAgents
print(response.choices[0].message.content)
# → Gets RLM's response
```

---

## Benefits

| Feature | Before | After |
|---------|--------|-------|
| **Code Changes** | Modify HyperAgents | ZERO changes |
| **Context** | Limited to prompt | Whole repo as context |
| **Reasoning** | Single LLM call | Recursive RLM reasoning |
| **Cost** | OpenAI API costs | Your API key (any provider) |
| **Flexibility** | Fixed model | Any backend RLM supports |

---

## Testing

### Test API Server

```bash
# Health check
curl http://localhost:8000/health

# Chat completion
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"What files are in this repo?"}]}'
```

### Test with HyperAgents

```bash
# 1. Start API server
uv run python -m rlcodar_hyperagi.api --port 8000

# 2. In another terminal, run HyperAgents
cd hyperagents
python meta_agent.py --repo_path=. --eval_path=./outputs
```

---

## Troubleshooting

### Server Won't Start

```bash
# Check if port 8000 is in use
lsof -ti:8000 | xargs kill -9

# Restart server
uv run python -m rlcodar_hyperagi.api --port 8000
```

### litellm Not Calling API

```bash
# Check .env file
cat hyperagents/.env

# Should have:
# OPENAI_BASE_URL=http://localhost:8000/v1
```

### RLM Not Loading Context

```bash
# Load files explicitly
curl -X POST http://localhost:8000/v1/rlm/load_context \
  -H "Content-Type: application/json" \
  -d '{"files":["./path/to/file.py"]}'
```

---

## Next Steps

1. **Start API server**: `uv run python -m rlcodar_hyperagi.api --port 8000`
2. **Configure HyperAgents**: Add OPENAI_BASE_URL to .env
3. **Run HyperAgents**: No code changes needed!
4. **Monitor**: Check `/v1/rlm/status` for RLM stats

---

**RLCoDAR-HyperAGI: HyperAgents with RLM reasoning, ZERO code changes!**
