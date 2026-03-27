# BMAD Workflow Map — bapXdi Adaptation

FOUR_PHASES:
Phase 1 analysis: capture requirements product requirements document PRD user stories
Phase 2 planning: break PRD into prioritized user stories sprint backlog
Phase 3 solutioning: architecture design implementation steps technical spec
Phase 4 implementation: iterative coding reviewing testing deploying

SCALE_ADAPTIVE:
simple: one agent one hop direct answer
medium: two agents two hops cross-reference
complex: three agents three hops multi-document synthesis
enterprise: full party mode all agents parallel hops federated knowledge

PARTY_MODE:
Multiple agent personas collaborate in single session.
Each agent reads its own document shard via RLM.
Language orchestrates parallel diffusion across all agents.
Outputs assembled by language into coherent multi-perspective response.

FEDERATED_KNOWLEDGE:
Git repositories become document shards — drop repo into user_docs/
Web pages become document shards — URL stored as reference in queries.json
Databases become document shards — SQL exports become .md files
All sources mapped by RLM — no central embedding index needed

CONTEXT_EVAPORATION_PREVENTION:
Traditional LLMs: context window fills up — earlier turns forgotten.
bapXdi: queries.json grows — all turns preserved with timestamps.
Crystallized output from each turn conditions next RLM hop.
Context never evaporates because documents are the memory.
