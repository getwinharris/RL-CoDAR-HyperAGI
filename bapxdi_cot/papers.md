# Foundation Papers Index

See specialist docs for full content:
  Bit Diffusion → docs/bit_diffusion.md
  Mercury 2     → docs/mercury2_thinking.md
  RLM           → cot/thinking.md
  Gemini Diff   → cot/gemini_diffusion_thinking.md
  BLT           → search query: byte latent transformer patches entropy
  AttnRes       → search query: kimi attention residuals depth aggregation
  Kimi Linear   → search query: kimi delta attention linear gated

Papers prove: docs are the model, diffusion generates, RLM routes.
See each specialist doc for implementation details.

PAPER 9: BUILDING PERSONAL INTELLIGENCE
Source: ai.google/static/documents/building_personal_intelligence.pdf
Google. January 2026. Srinivasan Venkatachary.

KEY INSIGHT: context packing problem
"enabling Gemini models to safely and accurately reason over
disparate and vast amounts of personal data sources in real-time"

KEY MECHANISM: continuous stream of context
"moving towards a world where products can securely access personal
information as a continuous stream of context to inform every interaction"

NO RETRAINING: adaptation through context not weights
"Gemini Apps don't train directly on your Gmail inbox or Google Photos library"
"To improve functionality over time, we train on prompts and responses and
summaries excerpts and inferences used to help answer your prompts"

BAPXDI IMPLEMENTS THIS NATIVELY:
queries.json = continuous stream of personal context
RLM reads it as a document shard = context packing
No separate Personal Intelligence Engine needed
The routing IS the engine
User's query history crystallized into replies = the model's memory of that user

PAPER 10: BAYESIAN TEACHING
research.google/blog/teaching-llms-to-reason-like-bayesians/
Google Research. March 2026.

MODEL UPDATES BELIEF ABOUT USER AFTER EACH TURN:
posterior = prior × likelihood
Prior = queries.json previous turns
Likelihood = did user continue? did they ask follow-up?
Posterior = updated queries.json = updated user model
Bayesian assistant reached 81% accuracy vs plateau for standard LLMs
Generalizes across domains — learned from flights, works on hotels

BAPXDI IMPLEMENTATION:
queries.json IS the posterior distribution over user preferences
Each turn: new query + new reply appended = posterior update
RLM reads queries.json = reads the posterior = Bayesian inference for free
No Bayesian model needed. Document IS the probability distribution.

PAPER 11: RL2F — Reinforcement Learning with Language Feedback
Google DeepMind. February 2026.

MODEL LEARNS FROM FEEDBACK WITHOUT RETRAINING:
Fast weights = temporary activations = context window
Slow weights = permanent trained parameters = equivalent to docs in bapXdi
RL2F trains slow weights to be responsive to feedback
bapXdi equivalent: user feedback written to docs/ = permanent slow weight update
Writing a markdown file = equivalent of gradient descent in weight space
Next query reads feedback doc = model has integrated the correction

AUTODIDACTIC LOOP:
User gives feedback → written to docs/users/feedback.md
RLM reads feedback doc next query → reply adapts
Over time → bapXdi knows this user's preferences from their document history
No retraining. No gradient. Just document writes and RLM reads.

PAPER 12: REASONING OVER MATHEMATICAL OBJECTS
hf.co/papers/2603.18886
Authors: Pranjal Aggarwal, Marjan Ghazvininejad et al. Meta FAIR + NYU. March 19 2026.

WHAT THE PAPER SAYS:
Mathematical reasoning needs formally structured expressions not just numbers.
Principia suite: benchmarks for deriving mathematical objects (matrices, polynomials, expressions).
On-policy judge training: model trains its own reward signal from its own outputs.
Test-time aggregation: more compute at inference = better math reasoning.
Qwen3-235B and o3 STRUGGLE on Principia — this is an open problem.

THREE CONTRIBUTIONS:
1. Principia suite — math object derivation training data and benchmarks
2. On-policy judge training — LLM judges its own output, boosts performance
3. Test-time compute scaling via aggregation — run multiple candidates, pick best

WHAT BAPXDI TAKES:

1. DATASET: Principia suite → add to HF_DATASETS as "math_objects" modality
   NuminaMath = CoT proofs (numerical answers)
   Principia = symbolic mathematical objects (matrices, expressions)
   Query "derive the eigenvalue matrix" → routes to math_objects dataset

2. ON-POLICY JUDGING = BM25 self-scoring
   After each diffusion hop, BM25 score of output vs NuminaMath signal
   Low score = output not mathematically structured → more hops
   This IS on-policy judging without a separate judge model
   The document IS the reward signal

3. TEST-TIME AGGREGATION = AttnRes already implements this
   Multiple RLM hops over NuminaMath = multiple candidates
   AttnRes weighted blend = aggregation by relevance score
   Higher compute (more hops) = better math output
   Already in v3.0 — mathematically correct

PAPER 13: ARC-AGI-3
arcprize.org/arc-agi/3 | arXiv 2601.10904
François Chollet, Mike Knoop. ARC Prize Foundation. March 26 2026 — TODAY.
$2M prize pool. Best AI: 12.58%. Humans: 100%.

CORE DEFINITION: Intelligence = skill-acquisition efficiency on novel tasks.
Not memorization. Not pattern matching. Not scale.
Three requirements ARC-1/2 lacked that ARC-3 demands:
  Exploration — navigate unknown environment with no map
  Goal acquisition — infer what the goal IS from observation  
  Efficiency scoring — fewer steps to goal = higher intelligence

DEFINING THEME OF 2025: refinement loops
Per-task iterative optimization guided by feedback signal.
RLM understanding refinement loop IS this.

BAPXDI METRICS FROM THIS PAPER:
  hop_efficiency = best_bm25_score / num_hops  (score per hop)
  Higher = more intelligent routing (fewer hops to reach good signal)
  exec_signal = BM25(output, signal) = implicit executor feedback

PAPER 14: HYPERAGENT
hf.co/papers/2409.16299
Huy Phan, Phong Nguyen, Nghi Bui. September 2024.
25.01% SWE-Bench-Lite. SOTA repository code generation.

FOUR AGENTS: Planner Navigator CodeEditor Executor
Direct mapping to bapXdi:
  Planner = mercury_think()
  Navigator = rlm_peek()
  Code Editor = diffuse_block()
  Executor = bm25_score(output, signal) = exec_signal

WHAT TO BUILD:
Multi-turn task decomposition: Planner writes subtasks to queries.json
Each subtask = one session turn = one RLM hop sequence
Executor feedback written back to session = refinement loop
Repository dropped in user_docs/ = Navigator has the codebase
