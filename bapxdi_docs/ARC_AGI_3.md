# ARC-AGI-3 — Interactive Reasoning Benchmark
Source: arcprize.org/arc-agi/3
Authors: François Chollet, Mike Knoop. ARC Prize Foundation.
Released: March 26, 2026 (TODAY). arXiv: 2601.10904

WHAT IT IS:
First interactive reasoning benchmark for AI agents.
Not static grid puzzles (ARC-1, ARC-2).
Novel video-game-like environments. No instructions. No stated goals.
Agent must: explore environment, infer rules, form strategy, reach goal.
Scored by efficiency — fewer steps = higher score.
Humans: 100%. Best AI so far: 12.58%. Frontier LLMs: under 1%.
$1M prize. All solutions must be open-source (MIT or CC0).
No internet access during Kaggle evaluation — no API calls.

CHOLLET'S CORE ARGUMENT:
Intelligence = skill-acquisition efficiency on novel tasks.
NOT memorization. NOT pattern matching. NOT scale.
ARC-AGI-3 requires: exploration, planning, memory, goal acquisition.
Refinement loops are now the key to ARC progress.
The defining theme of 2025 is the refinement loop.

ARC-AGI-3 REQUIRES:
  - Exploration: agent navigates unknown environment with no map
  - Planning: multi-step strategy toward unknown goal
  - Memory: track state across interactions
  - Goal acquisition: infer what the goal IS from observation
  - Alignment: pursue that inferred goal efficiently

KEY FINDING FROM PREVIEW:
Top three systems were NON-LLM approaches.
Graph search + state tracking + systematic exploration beat all LLMs.
CNN-based structured exploration beat GPT-5.x by 12+ points.
Raw model size does not matter for novel environment reasoning.

WHAT THIS MEANS FOR BAPXDI:
bapXdi already implements several ARC-AGI-3 requirements:

1. EXPLORATION = RLM hops over unknown document space
   Agent navigates docs with no pre-loaded map.
   Each hop discovers new information. Exactly like ARC-3 exploration.

2. MEMORY = queries.json + users/model.md
   Full interaction history. Bayesian posterior per user.
   State tracked across sessions, not just within one context.

3. GOAL ACQUISITION = mercury_think() CoT pass
   Infers what query really needs before generating.
   EASY/MEDIUM/HARD routing = goal classification.

4. REFINEMENT LOOP = RLM understanding refinement
   Each hop refines understanding of query.
   hop 1 → crystallize → hop 2 conditioned on hop 1 → closer to goal.
   This IS the refinement loop Chollet says is key.

WHAT BAPXDI STILL NEEDS FOR ARC-AGI-3:
  - Environment state tracking across multiple turns
  - Explicit goal inference: "what is the environment rewarding?"
  - Efficiency metric: minimize hops to reach correct answer
  - Graph-based exploration of document structure (not just BM25)
