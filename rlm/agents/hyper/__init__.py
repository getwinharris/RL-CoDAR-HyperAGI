"""
RLM Agents Module - HyperAgents Integration
Self-improving agent system from Meta AI

Imports directly from the vendored hyperagents/ directory.
"""

import sys
import os

# Add the monorepo root to sys.path so hyperagents/ is importable
_monorepo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if _monorepo_root not in sys.path:
    sys.path.insert(0, _monorepo_root)

from hyperagents.meta_agent import MetaAgent
from hyperagents.task_agent import TaskAgent

__all__ = [
    "MetaAgent",
    "TaskAgent",
]
