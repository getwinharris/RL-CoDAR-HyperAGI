BAPXDI AGENT SKILLS — BMAD COMPATIBLE SKILL ARCHITECTURE

SKILL: byte-diffusion-generate
Trigger: any generation query
1. Language routes to correct HF dataset by modality
2. Mercury CoT thinking — silent pass over cot/ docs
3. RLM recursive hops — peek at relevant doc windows
4. AttnRes weighted accumulation — higher relevance hops dominate
5. Gemini Diffusion block — all positions from noise simultaneously
6. 8-byte hardware alignment
7. Entropy safety check — refetch below 0.30

SKILL: rlm-document-navigation
Trigger: multi-hop reasoning query
1. Hop 1 — peek most relevant window, crystallize
2. Crystallized output joins accumulated context
3. Hop 2 — conditioned on accumulated context
4. Hop 3 HARD mode — deeper document navigation

SKILL: session-context
Trigger: ongoing conversation
1. Load queries.json — full previous turns
2. Extract last 5 crystallized outputs
3. Prepend context to new query
4. Generate with conditioned query
5. Save turn back to queries.json

SKILL: document-add
Trigger: file dropped in user_docs/
1. Read file bytes — no parsing no chunking
2. File immediately part of the model
3. Next query navigates it via RLM

SKILL: modality-route
math      → AI-MO/NuminaMath-CoT (860K olympiad problems)
code      → m-a-p/CodeFeedback (600+ languages)
audio     → facebook/voxpopuli (CC0, 18 languages)
image     → google-research-datasets/conceptual_captions
multilingual → CohereLabs/aya_dataset (65 languages)
web       → HuggingFaceFW/fineweb (18.5T tokens)
science   → HuggingFaceTB/smollm-corpus (Cosmopedia)
multihop  → hotpotqa/hotpot_qa (113K multi-hop)
default   → wikimedia/wikipedia (300+ languages)
