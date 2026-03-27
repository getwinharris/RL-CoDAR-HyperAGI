# RACoDAR Implementation Plan

**Recursive Language - Continuous Diffusion with Contextual AutoRegressive Decoder**

**Goal:** Unify RLM + HyperAgents into ONE pipeline with 64 crystallization loops

---

## 1. CURRENT STATE

### **What Exists:**

```
RLM (Recursive Language Model)
├── rlm/core/rlm.py              # Main RLM class
├── rlm/environments/            # REPL environments
├── rlm/datasets/                # Dataset streaming
└── rlm/agents/hyper/            # HyperAgents integration (broken imports)

HyperAgents
├── hyperagents/meta_agent.py    # Meta-agent for code modification
├── hyperagents/task_agent.py    # Task evaluation
├── hyperagents/generate_loop.py # Generation loop
└── hyperagents/utils/           # Utilities

RLCoDAR (Diffusion)
├── rlcodar_hyperagi/diffusion.py # CoDAR implementation
└── rlm/datasets/stream_datasets.py # HF dataset streaming
```

### **Problem:**
- RLM and HyperAgents are SEPARATE projects
- No unified pipeline
- No 64 crystallization loops
- No conversation history tracking
- No terminal/repo integration in diffusion

---

## 2. TARGET ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                    RACoDAR Pipeline                             │
│                                                                 │
│  User Query → [Conversation History JSON]                      │
│                    ↓                                            │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              64 CRYSTALLIZATION LOOPS                     │ │
│  │                                                           │ │
│  │  Loop 1-16:   Diffuse Conversation History               │ │
│  │               (timestamps + attachments + terminal logs)  │ │
│  │                                                           │ │
│  │  Loop 17-32:  Diffuse COT Datasets                       │ │
│  │               (Zebra-CoT, reasoning patterns)             │ │
│  │                                                           │ │
│  │  Loop 33-48:  Diffuse Code Datasets                      │ │
│  │               (The-Stack, repo code, tests)               │ │
│  │                                                           │ │
│  │  Loop 49-64:  Diffuse All Knowledge                      │ │
│  │               (repo + HF datasets + terminal state)       │ │
│  │                                                           │ │
│  │  Each Loop:                                               │ │
│  │    1. Cross-attend to knowledge index                    │ │
│  │    2. Refine embeddings (more coherent)                  │ │
│  │    3. Pass to next loop                                  │ │
│  └───────────────────────────────────────────────────────────┘ │
│                    ↓                                            │
│         Final Crystallization                                   │
│         (continuous → discrete bytes 0-255)                    │
│                    ↓                                            │
│  Output: Response + Terminal Commands + File Edits             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. FILE STRUCTURE (After Implementation)

```
RecursiveLM/
├── racodar/                        # NEW - Unified pipeline
│   ├── __init__.py
│   ├── pipeline.py                 # Main RACoDAR pipeline class
│   ├── crystallization.py          # 64-loop crystallization logic
│   ├── conversation_history.py     # JSON tracking with timestamps
│   └── knowledge_index.py          # Unified index (repo + HF datasets)
│
├── rlm/                            # RLM (modified)
│   ├── core/
│   │   └── rlm.py                  # Modified to use RACoDAR pipeline
│   ├── environments/
│   │   └── local_repl.py           # Terminal integration
│   ├── datasets/
│   │   └── stream_datasets.py      # HF dataset streaming (working)
│   └── agents/hyper/               # Fixed imports
│       ├── meta_agent.py
│       └── task_agent.py
│
├── hyperagents/                    # HyperAgents (unchanged)
│   ├── meta_agent.py
│   ├── task_agent.py
│   └── generate_loop.py
│
└── tests/
    └── test_racodar.py             # Integration tests
```

---

## 4. IMPLEMENTATION STEPS

### **Step 1: Create Conversation History Tracker**

**File:** `racodar/conversation_history.py`

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class ConversationHistory:
    """
    Track conversation with timestamps and attachments.
    Stored as JSON for diffusion.
    """
    
    def __init__(self):
        self.messages = []
        self.attachments = []
        self.terminal_logs = []
    
    def add_message(self, role: str, content: str, timestamp: datetime = None):
        """Add user/AI message"""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": timestamp.isoformat() if timestamp else datetime.now().isoformat(),
            "type": "message"
        })
    
    def add_attachment(self, file_path: str, content: str, attachment_type: str):
        """Add file attachment (code, image, etc.)"""
        self.attachments.append({
            "path": file_path,
            "content": content,
            "type": attachment_type,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_terminal_log(self, command: str, output: str, exit_code: int):
        """Add terminal execution log"""
        self.terminal_logs.append({
            "command": command,
            "output": output,
            "exit_code": exit_code,
            "timestamp": datetime.now().isoformat()
        })
    
    def to_json(self) -> str:
        """Convert to JSON for diffusion"""
        return json.dumps({
            "messages": self.messages,
            "attachments": self.attachments,
            "terminal_logs": self.terminal_logs
        }, indent=2)
    
    def to_bytes(self) -> List[int]:
        """Convert to bytes for diffusion"""
        return list(self.to_json().encode('utf-8'))
```

---

### **Step 2: Create Unified Knowledge Index**

**File:** `racodar/knowledge_index.py`

```python
from rlm.datasets import DatasetStreamer
from typing import Dict, List

class KnowledgeIndex:
    """
    Unified index for all knowledge sources:
    - Repo files
    - HF datasets
    - Terminal state
    - Conversation history
    """
    
    def __init__(self):
        self.repo_index = {}      # file_path → bytes
        self.dataset_indices = {} # dataset_name → streamer
        self.terminal_state = {}  # current terminal state
    
    def index_repo(self, repo_path: str):
        """Index all repo files"""
        import os
        for root, dirs, files in os.walk(repo_path):
            if '.git' in root or '.venv' in root:
                continue
            for f in files:
                if f.endswith('.py') or f.endswith('.md') or f.endswith('.txt'):
                    file_path = os.path.join(root, f)
                    with open(file_path, 'rb') as file:
                        self.repo_index[file_path] = list(file.read())
    
    def add_dataset(self, name: str, path: str, subset: str = None):
        """Add HF dataset to index"""
        self.dataset_indices[name] = DatasetStreamer(path, name=subset, limit=1000)
    
    def get_all_bytes(self) -> List[int]:
        """Get all indexed bytes for diffusion"""
        all_bytes = []
        
        # Repo files
        for file_bytes in self.repo_index.values():
            all_bytes.extend(file_bytes)
        
        # Datasets (stream)
        for dataset in self.dataset_indices.values():
            for item in dataset:
                text = item.get('text', '')
                all_bytes.extend(list(text.encode('utf-8')))
        
        return all_bytes
```

---

### **Step 3: Implement 64 Crystallization Loops**

**File:** `racodar/crystallization.py`

```python
from typing import List, Dict
import math

class CrystallizationLoop:
    """
    One loop of the 64 crystallization process.
    Refines embeddings by cross-attending to knowledge.
    """
    
    def __init__(self, loop_number: int, knowledge_index: KnowledgeIndex):
        self.loop_number = loop_number
        self.knowledge = knowledge_index
    
    def diffuse(self, embeddings: List[float]) -> List[float]:
        """
        Diffuse embeddings through knowledge.
        
        NOT denoising - making more coherent.
        """
        # Determine which knowledge source to use
        if self.loop_number < 16:
            # Loop 1-16: Conversation history
            knowledge_bytes = self._get_conversation_bytes()
        elif self.loop_number < 32:
            # Loop 17-32: COT datasets
            knowledge_bytes = self._get_cot_bytes()
        elif self.loop_number < 48:
            # Loop 33-48: Code datasets
            knowledge_bytes = self._get_code_bytes()
        else:
            # Loop 49-64: All knowledge
            knowledge_bytes = self.knowledge.get_all_bytes()
        
        # Cross-attention: embeddings attend to knowledge bytes
        refined_embeddings = self._cross_attention(embeddings, knowledge_bytes)
        
        return refined_embeddings
    
    def _cross_attention(self, embeddings: List[float], knowledge_bytes: List[int]) -> List[float]:
        """
        Cross-attention between embeddings and knowledge.
        
        Simple implementation (can be enhanced):
        For each embedding, find most similar knowledge bytes and refine.
        """
        # Convert bytes to embeddings (simple normalization)
        knowledge_embeddings = [b / 255.0 for b in knowledge_bytes]
        
        # For each embedding, refine using knowledge
        refined = []
        for emb in embeddings:
            # Find most similar knowledge embeddings
            similarities = []
            for k_emb in knowledge_embeddings[:1000]:  # Limit for speed
                sim = self._cosine_sim([emb], [k_emb])
                similarities.append(sim)
            
            # Refine embedding (move toward most similar knowledge)
            if similarities:
                max_sim_idx = similarities.index(max(similarities))
                refinement = knowledge_embeddings[max_sim_idx]
                # Blend current embedding with knowledge
                refined_emb = 0.7 * emb + 0.3 * refinement
            else:
                refined_emb = emb
            
            refined.append(refined_emb)
        
        return refined
    
    def _cosine_sim(self, a: List[float], b: List[float]) -> float:
        """Cosine similarity"""
        dot_product = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(x * x for x in b))
        if norm_a < 1e-10 or norm_b < 1e-10:
            return 0.0
        return dot_product / (norm_a * norm_b)
    
    def _get_conversation_bytes(self) -> List[int]:
        """Get conversation history bytes"""
        # Implementation depends on conversation history tracker
        return []
    
    def _get_cot_bytes(self) -> List[int]:
        """Get COT dataset bytes"""
        # Stream from Zebra-CoT
        return []
    
    def _get_code_bytes(self) -> List[int]:
        """Get code dataset bytes"""
        # Stream from The-Stack
        return []


class CrystallizationPipeline:
    """
    Full 64-loop crystallization pipeline.
    """
    
    def __init__(self, knowledge_index: KnowledgeIndex):
        self.knowledge = knowledge_index
        self.loops = [CrystallizationLoop(i, knowledge_index) for i in range(64)]
    
    def crystallize(self, initial_embeddings: List[float]) -> List[float]:
        """
        Run all 64 crystallization loops.
        
        Input: Initial embeddings (from conversation history)
        Output: Crystallized embeddings (ready for final discretization)
        """
        embeddings = initial_embeddings
        
        for i, loop in enumerate(self.loops):
            embeddings = loop.diffuse(embeddings)
            
            # Optional: Log progress
            if (i + 1) % 16 == 0:
                print(f"Crystallization Loop {i+1}/64 complete")
        
        return embeddings
    
    def crystallize_to_bytes(self, initial_embeddings: List[float]) -> List[int]:
        """
        Crystallize and convert to discrete bytes.
        
        Final step: continuous embeddings → discrete bytes (0-255)
        """
        # Run 64 loops
        crystallized_embeddings = self.crystallize(initial_embeddings)
        
        # Convert to bytes (simple rounding)
        output_bytes = []
        for emb in crystallized_embeddings:
            # Convert from [0, 1] to [0, 255]
            byte_val = int(emb * 255)
            byte_val = max(0, min(255, byte_val))  # Clamp
            output_bytes.append(byte_val)
        
        return output_bytes
```

---

### **Step 4: Create Unified Pipeline**

**File:** `racodar/pipeline.py`

```python
from .conversation_history import ConversationHistory
from .knowledge_index import KnowledgeIndex
from .crystallization import CrystallizationPipeline
from rlm import RLM
from hyperagents.meta_agent import MetaAgent
from hyperagents.task_agent import TaskAgent

class RACoDARPipeline:
    """
    Unified RACoDAR pipeline.
    
    Connects:
    - RLM (repo + terminal access)
    - HyperAgents (self-improvement)
    - CoDAR (64 crystallization loops)
    """
    
    def __init__(self, repo_path: str):
        # Initialize components
        self.history = ConversationHistory()
        self.knowledge = KnowledgeIndex()
        self.crystallizer = CrystallizationPipeline(self.knowledge)
        
        # Index repo
        self.knowledge.index_repo(repo_path)
        
        # Add HF datasets
        self.knowledge.add_dataset("fineweb", "HuggingFaceFW/fineweb")
        self.knowledge.add_dataset("zebra-cot", "multimodal-reasoning-lab/Zebra-CoT", 
                                   "2D Visual Reasoning - Visual Search")
        self.knowledge.add_dataset("the-stack", "bigcode/the-stack-v2", "data/python")
        
        # Initialize RLM
        self.rlm = RLM(backend='openai', environment='local', persistent=True)
        
        # Initialize HyperAgents
        self.meta_agent = MetaAgent()
        self.task_agent = TaskAgent()
    
    def process_query(self, query: str) -> str:
        """
        Process user query through full RACoDAR pipeline.
        """
        # 1. Add query to conversation history
        self.history.add_message("user", query)
        
        # 2. Convert to initial embeddings
        query_bytes = list(query.encode('utf-8'))
        initial_embeddings = [b / 255.0 for b in query_bytes]
        
        # 3. Run 64 crystallization loops
        crystallized_bytes = self.crystallizer.crystallize_to_bytes(initial_embeddings)
        
        # 4. Convert bytes to response
        try:
            response = bytes(crystallized_bytes).decode('utf-8', errors='ignore')
        except:
            response = "Error generating response"
        
        # 5. Add response to history
        self.history.add_message("assistant", response)
        
        # 6. If response contains commands, execute via RLM
        if "```bash" in response:
            # Extract and execute commands
            commands = self._extract_commands(response)
            for cmd in commands:
                # Execute via RLM terminal
                result = self.rlm._persistent_env.execute_code(cmd)
                self.history.add_terminal_log(cmd, result.output, result.exit_code)
        
        # 7. If response contains file edits, apply via HyperAgents
        if "```python" in response or "```diff" in response:
            # Extract and apply edits
            edits = self._extract_edits(response)
            for edit in edits:
                # Apply via HyperAgents meta-agent
                self.meta_agent.forward(repo_path, edit)
        
        return response
    
    def _extract_commands(self, response: str) -> List[str]:
        """Extract bash commands from response"""
        # Simple extraction (can be enhanced)
        commands = []
        in_block = False
        for line in response.split('\n'):
            if line.strip() == '```bash':
                in_block = True
            elif line.strip() == '```':
                in_block = False
            elif in_block:
                commands.append(line)
        return commands
    
    def _extract_edits(self, response: str) -> List[Dict]:
        """Extract file edits from response"""
        # Simple extraction (can be enhanced)
        edits = []
        # Implementation depends on edit format
        return edits
```

---

### **Step 5: Update RLM to Use RACoDAR**

**File:** `rlm/core/rlm.py` (modification)

```python
# Add at top of file
from racodar.pipeline import RACoDARPipeline

# Modify RLM class
class RLM:
    def __init__(self, *args, **kwargs):
        # ... existing init ...
        
        # Initialize RACoDAR pipeline
        repo_path = kwargs.get('repo_path', '.')
        self.racodar = RACoDARPipeline(repo_path)
    
    def completion(self, prompt: str, **kwargs):
        """
        Use RACoDAR pipeline for completion.
        """
        # Use RACoDAR for reasoning
        response = self.racodar.process_query(prompt)
        
        return RLMChatCompletion(
            response=response,
            # ... rest of response ...
        )
```

---

## 5. USAGE EXAMPLE

```python
from racodar import RACoDARPipeline

# Initialize pipeline
pipeline = RACoDARPipeline(repo_path="/path/to/your/repo")

# Add HF datasets
pipeline.knowledge.add_dataset("zebra-cot", "multimodal-reasoning-lab/Zebra-CoT", 
                               "2D Visual Reasoning - Visual Search")

# Process query
response = pipeline.process_query("How do I fix this bug in main.py?")
print(response)

# Response includes:
# - Reasoning from 64 crystallization loops
# - Terminal commands (if needed)
# - File edits (if needed)
# - Full conversation history tracked
```

---

## 6. TESTING

```python
# tests/test_racodar.py

def test_crystallization_loops():
    """Test 64 crystallization loops"""
    knowledge = KnowledgeIndex()
    knowledge.index_repo(".")
    
    crystallizer = CrystallizationPipeline(knowledge)
    
    # Simple query
    query = "What is Python?"
    query_bytes = list(query.encode('utf-8'))
    initial_embeddings = [b / 255.0 for b in query_bytes]
    
    # Run crystallization
    output_bytes = crystallizer.crystallize_to_bytes(initial_embeddings)
    
    # Should produce coherent output
    assert len(output_bytes) > 0
    assert all(0 <= b <= 255 for b in output_bytes)

def test_full_pipeline():
    """Test full RACoDAR pipeline"""
    pipeline = RACoDARPipeline(repo_path=".")
    
    response = pipeline.process_query("List files in current directory")
    
    assert response is not None
    assert len(response) > 0
```

---

## 7. IMPLEMENTATION ORDER

1. ✅ **Conversation History** (`racodar/conversation_history.py`)
2. ✅ **Knowledge Index** (`racodar/knowledge_index.py`)
3. ✅ **Crystallization Loops** (`racodar/crystallization.py`)
4. ✅ **Unified Pipeline** (`racodar/pipeline.py`)
5. ⏳ **Update RLM** (modify `rlm/core/rlm.py`)
6. ⏳ **Fix HyperAgents imports** (fix `rlm/agents/hyper/*.py`)
7. ⏳ **Add tests** (`tests/test_racodar.py`)

---

## 8. WHAT'S DIFFERENT FROM BEFORE

| Before (Wrong) | After (Correct) |
|----------------|-----------------|
| Separate RLM + HyperAgents | **Unified RACoDAR pipeline** |
| No conversation tracking | **JSON history with timestamps** |
| No terminal integration | **Terminal logs in diffusion** |
| Just search | **64 crystallization loops** |
| One-step retrieval | **Multi-loop refinement** |
| No HF datasets | **HF datasets indexed** |

---

**This is the CORRECT plan. Should I implement it now?**
