# HyperAgent — Generalist Software Engineering Agent
hf.co/papers/2409.16299
Authors: Huy Nhat Phan, Phong X. Nguyen, Nghi D. Q. Bui. September 2024.

WHAT IT IS:
Multi-agent system for software engineering across full task lifecycle.
Four specialized agents: Planner, Navigator, Code Editor, Executor.
25.01% on SWE-Bench-Lite, 31.40% on SWE-Bench-Verified.
SOTA on repository-level code generation (RepoExec).
SOTA on fault localization and program repair (Defects4J).
Handles GitHub issue resolution end-to-end.

FOUR AGENT STRUCTURE:
  PLANNER:   Breaks down SE task into subtasks. Makes the plan.
  NAVIGATOR: Explores codebase. Finds relevant files/functions.
  CODE EDITOR: Makes targeted changes. Understands diffs.
  EXECUTOR:  Runs code. Gets feedback. Reports results.

HOW THEY COLLABORATE:
  User issue → Planner → plan → Navigator finds relevant code
  → Code Editor makes change → Executor runs test
  → if fail → feedback back to Planner → refinement loop
  This IS the ARC-AGI-3 refinement loop applied to code.

THE KEY INSIGHT:
Navigator = RLM. It browses the codebase looking for relevant context.
Code Editor = diffusion. It modifies bytes in targeted positions.
Executor = evaluation. It checks if the diff was correct.
Planner = mercury_think(). It decides what to do before doing it.

FOR BAPXDI — DIRECT MAPPING:
  HyperAgent Planner    ↔ mercury_think() — decides complexity before acting
  HyperAgent Navigator  ↔ rlm_peek() — finds relevant doc/code windows
  HyperAgent Code Editor ↔ diffuse_block() — modifies byte positions
  HyperAgent Executor   ↔ bm25_score() — evaluates if output matched goal
  
WHAT TO TAKE:
1. REPOSITORY AS DOCUMENT
   Drop any GitHub repo into user_docs/ → it is the model.
   Navigator = RLM hopping over repo files.
   No embedding index. BM25 over source file bytes.
   
2. EXECUTOR FEEDBACK LOOP
   After diffusion produces code:
   BM25 score of output vs target doc = implicit execution score.
   Low score = code probably wrong → more hops → refine.
   This IS the executor feedback without running actual code.
   
3. FOUR-PERSONA ACTIVATION
   bapXdi already has these personas in docs/bmad/agents/:
   architect.md = Planner
   developer.md = Code Editor  
   researcher.md = Navigator (but over docs not code)
   qa-engineer.md = Executor
   Activate them via persona selection per subtask.

WHAT BAPXDI NEEDS FROM HYPERAGENT:
  - Multi-turn task decomposition (Planner writes subtasks to queries.json)
  - Navigator persona that explicitly browses repo structure
  - Executor that verifies output against test cases
  - Feedback loop from Executor back to Planner (write result to session)
