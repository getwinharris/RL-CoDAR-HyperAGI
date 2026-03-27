# Google Bayesian Teaching + RL2F
# Two papers that define how bapXdi should adapt to each user

================================================================================
PAPER A: BAYESIAN TEACHING
================================================================================
Source: research.google/blog/teaching-llms-to-reason-like-bayesians/
Google Research. March 2026.

WHAT IT SAYS:
LLM needs to infer user preferences gradually from choices over multiple turns.
Bayesian inference defines the optimal way to perform such updates.
The Bayesian assistant maintains a probability distribution over possible user
preferences and updates it using Bayes' rule after each interaction.
Standard LLMs plateau almost immediately — they do not update internal beliefs.
Bayesian-tuned models reached 81% accuracy vs plateau for standard LLMs.
Generalizes to new domains: trained on flights, works on hotels, web shopping.

THE CORE PRINCIPLE:
After each interaction: posterior = prior × likelihood / evidence
Prior = what we knew about user before this query
Likelihood = probability user would ask this given their preference profile
Posterior = updated belief about user preferences
Next reply is conditioned on posterior — not just the raw query

FOR BAPXDI:
queries.json IS the posterior. Each turn updates it.
Prior = previous turns in queries.json
Likelihood = how well this reply matched what user wanted (did they continue?)
Posterior = updated queries.json with new turn appended
RLM reads queries.json each time = reading the posterior = Bayesian update
No separate Bayesian model needed. The document IS the posterior distribution.

================================================================================
PAPER B: RL2F — Reinforcement Learning with Language Feedback
================================================================================
Source: Google DeepMind. February 2026.

WHAT IT SAYS:
Current LLMs have zero in-context plasticity on feedback integration.
Model verbally acknowledges feedback but does not integrate it.
RL2F fuses In-Context Learning + Reinforcement Learning with Verifiable Rewards.
Teacher model provides language feedback (not the answer — just guidance).
Student uses feedback to revise its solution.
Multi-turn interaction history becomes training data.
Result: model that genuinely learns from correction within a conversation.
Eventually becomes autodidactic — corrects itself without external teacher.

KEY INSIGHT — fast weights vs slow weights:
Fast weights = activations, context window, temporary per-forward-pass
Slow weights = trained parameters, permanent
Standard LLMs: feedback goes into fast weights but slow weights ignore it
RL2F: trains slow weights to make fast weights responsive to feedback

FOR BAPXDI — without training:
bapXdi has no slow weights. Everything IS fast weights = the documents.
When user gives feedback: write it to docs/ as a new shard.
That new shard IS the slow weight update — permanent, read every time.
No gradient descent. The document write IS the weight update.
RLM reads the feedback doc on the next query = RL2F without RL.
The docs ARE the slow weights. Writing to docs = training.

================================================================================
HOW THESE TWO PAPERS WORK TOGETHER IN BAPXDI
================================================================================

TURN 1: user asks "explain bit diffusion"
  Prior: queries.json is empty. No user model yet.
  RLM peeks: finds bit_diffusion.md. Crystallizes reply.
  Saves to queries.json: {query, reply, ts}

TURN 2: user asks "how does it compare to regular transformers"
  Prior: queries.json has Turn 1 — user is interested in diffusion architecture
  Bayesian update: user is technical, wants comparisons, not introductions
  RLM peeks: reads queries.json (prior) + finds OMNI_ARCHITECTURE.md
  Posterior: queries.json now has Turn 1 + Turn 2

TURN N: user gives feedback "that reply was too technical"
  RL2F mechanism: write feedback to docs/users/bapX_feedback.md
  Next query: RLM reads feedback doc — now knows user prefers simpler language
  Slow weight equivalent: the feedback doc is permanent
  Model permanently adapted to this user. No retraining. Just documents.

RESULT:
  Each user has their own queries.json = their own posterior = their own model
  One diffusion kernel. Millions of unique user models.
  Adaptation is free. Writing to a text file. That is all.
