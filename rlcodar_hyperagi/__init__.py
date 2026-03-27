"""
RLCoDAR-HyperAGI: Unified Package

OpenAI-compatible API server connecting HyperAgents to RLM.

Usage:
    python -m rlcodar_hyperagi.api --port 8000

Then configure HyperAgents (.env):
    OPENAI_BASE_URL=http://localhost:8000/v1
    OPENAI_API_KEY=not-needed
"""

from rlcodar_hyperagi.api import app, main

__version__ = "1.0.0"
__all__ = ["app", "main"]
