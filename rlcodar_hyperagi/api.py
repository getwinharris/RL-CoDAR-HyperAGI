"""
RLCoDAR-HyperAGI: OpenAI-Compatible API Server

CoDAR IS the model. No external LLM calls.
Indexes repo bytes + datasets, reasons via diffusion, returns passages.

Usage:
    python -m rlcodar_hyperagi.api --port 8000

The API key is OpenAI-compatible but serves OUR model:
    Authorization: Bearer rlcodar-...
"""

import os
import sys
import time
import json
from typing import List, Dict, Any, Optional

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rlcodar_hyperagi.diffusion import (
    CoDARDiffusion,
    ByteIndex,
    CosineNoiseSchedule,
    ByteGroupTokenizer,
)

try:
    from fastapi import FastAPI, HTTPException, Security
    from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
    from pydantic import BaseModel
    import uvicorn
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False

# Master API key — OUR model's key, OpenAI-compatible format
MASTER_API_KEY = os.getenv(
    "RLCODAR_API_KEY",
    "rlcodar-3f7c5f8231d7ad7f7c1629a09c4214c41fa6df00d7d83ec38966978c1ec2d398"
)

# Global CoDAR instance
_codar: Optional[CoDARDiffusion] = None
_index: Optional[ByteIndex] = None


def init_codar(repo_root: str = None):
    """
    Initialize CoDAR by indexing repo files.

    This is the "model loading" step — the index IS the weights.
    """
    global _codar, _index

    if repo_root is None:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print(f"📄 Indexing repo: {repo_root}")

    _index = ByteIndex()
    total = _index.add_directory(repo_root)

    schedule = CosineNoiseSchedule(T=100)
    tokenizer = ByteGroupTokenizer()
    _codar = CoDARDiffusion(_index, schedule, tokenizer)

    print(f"✅ CoDAR initialized: {_index.stats['total_groups']} groups from {_index.stats['total_sources']} sources ({_index.stats['total_bytes']} bytes)")

    return _codar


# ============================================================================
# CLI Mode (no FastAPI needed)
# ============================================================================

def cli_completion(prompt: str) -> str:
    """Run a completion in CLI mode."""
    global _codar
    if _codar is None:
        init_codar()
    return _codar.completion(prompt)


def cli_repl():
    """Interactive REPL mode."""
    global _codar
    if _codar is None:
        init_codar()

    print("\n🤖 RLCoDAR REPL (type 'quit' to exit)\n")
    while True:
        try:
            prompt = input(">>> ")
            if prompt.strip().lower() in ('quit', 'exit', 'q'):
                break
            if not prompt.strip():
                continue
            response = _codar.completion(prompt)
            print(f"\n{response}\n")
        except (KeyboardInterrupt, EOFError):
            break
    print("\nBye!")


# ============================================================================
# FastAPI Server Mode
# ============================================================================

if HAS_FASTAPI:
    app = FastAPI(
        title="RLCoDAR-HyperAGI API",
        description="CoDAR byte-level diffusion model — OpenAI-compatible",
        version="2.0.0"
    )

    security = HTTPBearer(auto_error=False)

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
        """Verify API key."""
        if credentials is None:
            raise HTTPException(status_code=401, detail="Missing API key")
        if credentials.credentials != MASTER_API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API key")
        return credentials.credentials

    @app.on_event("startup")
    async def startup_event():
        """Index repo on startup — this IS model loading."""
        init_codar()

    @app.get("/health")
    async def health():
        return {
            "status": "healthy",
            "service": "rlcodar-hyperagi",
            "model": "codar",
            "indexed": _index.stats if _index else {},
        }

    @app.get("/v1/models")
    async def list_models():
        return {
            "object": "list",
            "data": [{
                "id": "rlcodar",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "rlcodar-hyperagi"
            }]
        }

    @app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
    async def chat_completions(
        request: ChatCompletionRequest,
        api_key: str = Security(verify_api_key)
    ):
        """CoDAR completion — no external LLM calls."""
        if _codar is None:
            raise HTTPException(status_code=503, detail="CoDAR not initialized")

        prompt = request.messages[-1].content

        try:
            response_text = _codar.completion(prompt)

            input_tokens = len(prompt.encode('utf-8'))
            output_tokens = len(response_text.encode('utf-8'))

            return ChatCompletionResponse(
                id=f"rlcodar-{int(time.time() * 1000)}",
                created=int(time.time()),
                model=request.model,
                choices=[{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": response_text
                    },
                    "finish_reason": "stop"
                }],
                usage={
                    "prompt_tokens": input_tokens,
                    "completion_tokens": output_tokens,
                    "total_tokens": input_tokens + output_tokens
                }
            )

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/v1/rlm/status")
    async def rlm_status():
        """CoDAR model status."""
        if _index is None:
            return {"status": "not_initialized"}
        return {
            "status": "ready",
            "model": "codar",
            "backend": "pure-python-diffusion",
            "index": _index.stats,
            "sources": list(_index.sources.keys())[:20],
        }

    @app.post("/v1/rlm/load_context")
    async def load_context(
        files: List[str],
        api_key: str = Security(verify_api_key)
    ):
        """Add files to the byte index."""
        if _index is None:
            raise HTTPException(status_code=503, detail="CoDAR not initialized")

        loaded = []
        for file_path in files:
            try:
                count = _index.add_file(file_path)
                loaded.append({
                    "path": file_path,
                    "groups": count,
                    "status": "indexed"
                })
            except Exception as e:
                loaded.append({
                    "path": file_path,
                    "status": "error",
                    "error": str(e)
                })

        return {"loaded": loaded}


def main():
    """Run API server or CLI."""
    import argparse

    parser = argparse.ArgumentParser(description="RLCoDAR-HyperAGI")
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--repl", action="store_true", help="Run in REPL mode")
    parser.add_argument("--query", type=str, help="Single query mode")
    parser.add_argument("--repo", type=str, help="Repo root to index")

    args = parser.parse_args()

    if args.query:
        if args.repo:
            init_codar(args.repo)
        else:
            init_codar()
        print(cli_completion(args.query))
        return

    if args.repl:
        if args.repo:
            init_codar(args.repo)
        else:
            init_codar()
        cli_repl()
        return

    if not HAS_FASTAPI:
        print("❌ FastAPI not installed. Use --repl or --query mode, or: pip install fastapi uvicorn")
        return

    print(f"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🚀 RLCoDAR-HyperAGI API Server v2.0                   ║
║   CoDAR Byte-Level Diffusion Model                       ║
║   No external LLM — pure Python inference                ║
║                                                          ║
║   Host: {args.host:<42} ║
║   Port: {args.port:<42} ║
║                                                          ║
║   Endpoints:                                             ║
║   POST /v1/chat/completions  (OpenAI-compatible)         ║
║   GET  /v1/models                                        ║
║   GET  /health                                           ║
║   GET  /v1/rlm/status                                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)

    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
