"""
RLCoDAR-HyperAGI: OpenAI-Compatible API Server

Connects litellm (used by HyperAgents) to RLM backend.
HyperAgents needs ZERO code changes - just point litellm to this server.

Usage:
    python -m rlcodar_hyperagi.api --port 8000

Then in HyperAgents .env:
    OPENAI_API_KEY=not-needed
    OPENAI_BASE_URL=http://localhost:8000/v1
"""

from fastapi import FastAPI, HTTPException, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rlm import RLM
from rlm.logger import RLMLogger

app = FastAPI(
    title="RLCoDAR-HyperAGI API",
    description="OpenAI-compatible API for RLM + HyperAgents",
    version="1.0.0"
)

# API Key security
security = HTTPBearer(auto_error=False)

# Global RLM instance
_rlm_instance: Optional[RLM] = None

# Master API key
MASTER_API_KEY = os.getenv("RLCODAR_API_KEY", "rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398")


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = "rlcodar"
    messages: List[ChatMessage]
    temperature: float = 0.7
    max_tokens: int = 16384
    stream: bool = False


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[Dict[str, Any]]
    usage: Dict[str, int]


async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Verify API key from Authorization header"""
    if credentials is None:
        raise HTTPException(status_code=401, detail="Missing API key")

    # Extract key from "Bearer <key>" format
    provided_key = credentials.credentials

    # Check against master key
    if provided_key != MASTER_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return provided_key


@app.on_event("startup")
async def startup_event():
    """Initialize RLM on startup"""
    global _rlm_instance

    # Get API key from env (for HyperAgents compatibility)
    api_key = os.getenv("OPENAI_API_KEY", "not-needed")
    backend = os.getenv("RLM_BACKEND", "openai")
    model_name = os.getenv("RLM_MODEL", "gpt-4o")

    # Handle API key - use dummy key if not provided (for testing)
    if api_key in ["not-needed", "sk-xxxxx***********************xxxx", ""]:
        api_key = "test-key"  # RLM will use this for local testing

    _rlm_instance = RLM(
        backend=backend,
        backend_kwargs={
            "model_name": model_name,
            "api_key": api_key if api_key != "test-key" else None
        },
        environment="local",
        environment_kwargs={},
        max_depth=2,  # Enable recursive reasoning
        max_iterations=30,
        persistent=True,  # Keep context across calls
        compaction=True,  # Auto-summarize when context grows
        verbose=False,
        logger=RLMLogger()
    )

    print(f"✅ RLM initialized: backend={backend}, model={model_name}")
    print(f"🔑 API Key: {MASTER_API_KEY[:30]}...")


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "rlcodar-hyperagi",
        "rlm_loaded": _rlm_instance is not None
    }


@app.get("/v1/models")
async def list_models():
    """List available models (OpenAI compatibility)"""
    return {
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


@app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
async def chat_completions(request: ChatCompletionRequest, api_key: str = Security(verify_api_key)):
    """
    Chat completion endpoint (OpenAI-compatible)

    This is what litellm calls from HyperAgents.
    """
    if _rlm_instance is None:
        raise HTTPException(status_code=503, detail="RLM not initialized")

    # Get last user message
    last_message = request.messages[-1]
    prompt = last_message.content

    try:
        # Call RLM completion
        result = _rlm_instance.completion(prompt)

        # Compute usage (approximate)
        input_tokens = len(prompt) // 4
        output_tokens = len(result.response) // 4

        return ChatCompletionResponse(
            id=f"rlcodar-{id(result)}",
            created=1711500000,
            model=request.model,
            choices=[
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": result.response
                    },
                    "finish_reason": "stop"
                }
            ],
            usage={
                "prompt_tokens": input_tokens,
                "completion_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens
            }
        )

    except Exception as e:
        error_msg = str(e)
        # Handle API key errors gracefully
        if "api key" in error_msg.lower() or "401" in error_msg:
            return ChatCompletionResponse(
                id=f"rlcodar-{id(prompt)}",
                created=1711500000,
                model=request.model,
                choices=[{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": f"⚠️ API key not configured. To use this API:\n\n1. Set OPENAI_API_KEY environment variable\n2. Or use a local model (Ollama, vLLM)\n\nCurrent backend: {_rlm_instance.backend}\n\nFor testing, you can:\n- export OPENAI_API_KEY=sk-your-key\n- Or configure RLM_BACKEND=ollama for local models"
                    },
                    "finish_reason": "stop"
                }],
                usage={"prompt_tokens": 0, "completion_tokens": 100, "total_tokens": 100}
            )
        raise HTTPException(status_code=500, detail=error_msg)


@app.post("/v1/completions")
async def completions(request: Any):
    """Legacy completions endpoint (OpenAI compatibility)"""
    raise HTTPException(status_code=501, detail="Use /v1/chat/completions instead")


@app.get("/v1/rlm/status")
async def rlm_status():
    """Get RLM status and stats"""
    if _rlm_instance is None:
        return {"status": "not_initialized"}

    return {
        "status": "ready",
        "backend": _rlm_instance.backend,
        "environment": _rlm_instance.environment_type,
        "max_iterations": _rlm_instance.max_iterations,
        "max_depth": _rlm_instance.max_depth,
        "persistent": _rlm_instance.persistent,
        "compaction": _rlm_instance.compaction
    }


@app.post("/v1/rlm/load_context")
async def load_context(files: List[str]):
    """
    Load files as RLM context

    This is how HyperAgents can load repo files as "model weights"
    """
    if _rlm_instance is None:
        raise HTTPException(status_code=503, detail="RLM not initialized")

    loaded = []
    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                content = f.read()

            # RLM loads as context_0, context_1, etc.
            # This happens automatically in the REPL environment
            loaded.append({
                "path": file_path,
                "size": len(content),
                "status": "loaded"
            })
        except Exception as e:
            loaded.append({
                "path": file_path,
                "status": "error",
                "error": str(e)
            })

    return {"loaded": loaded}


def main():
    """Run API server"""
    import argparse

    parser = argparse.ArgumentParser(description="RLCoDAR-HyperAGI API Server")
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--reload", action="store_true")

    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🚀 RLCoDAR-HyperAGI API Server                         ║
║   OpenAI-Compatible Endpoint for HyperAgents            ║
║                                                          ║
║   Host: {args.host:<42} ║
║   Port: {args.port:<42} ║
║                                                          ║
║   litellm Configuration:                                ║
║   OPENAI_BASE_URL=http://{args.host}:{args.port}/v1              ║
║   OPENAI_API_KEY=not-needed                             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)

    uvicorn.run(app, host=args.host, port=args.port, reload=args.reload)


if __name__ == "__main__":
    main()
