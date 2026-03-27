MERCURY 2 — THINKING AND DIFFUSION

Inception Labs 2026. arXiv 2506.17298

CORE DIFFERENCE FROM AUTOREGRESSIVE:
Autoregressive: token 1 then token 2 then token 3. Sequential. Slow.
Mercury: all positions noisy simultaneously. Refine in parallel. Fast.
Speed: 1109 tokens per second on H100.
Parallel refinement not sequential prediction.

THINKING BEFORE GENERATING:
CoT reasoning happens before output crystallizes.
Thinking is internal. Not narrated to user.
Model thinks using document context.
Then generates full answer in parallel diffusion steps.
Thinking = silent reasoning pass over document bytes.
Generating = diffusion crystallizing the answer.

COARSE TO FINE:
Step 1: rough shape of answer emerges from noise.
Step 2: high confidence words lock in.
Step 3: uncertain words conditioned on locked words.
Step 4: full coherent answer crystallized.
Not left to right. All positions simultaneously refined.

DOCUMENT AS CONTEXT NOT PROMPT:
Document bytes feed the diffusion conditioning signal.
Not stuffed into context window.
Not summarized.
Not compressed.
Raw bytes condition each denoising step.
Document stays external. Query drives the diffusion direction.

BAPXDI EXTENSION:
Mercury 2 still uses trained weights underneath.
bapXdi removes the trained weights.
Document bytes replace the weight matrix entirely.
Diffusion kernel reads document bytes as the denoising signal.
No training. No weight file. Document is the model.

PARALLEL MODALITIES:
Language thinks first.
Language decides which modality needed.
Image diffusion runs parallel to audio diffusion.
Video diffusion runs parallel to text diffusion.
Language assembles all outputs.
All modalities byte streams simultaneously denoising.

MERCURY 2 UNIQUE IDENTIFIERS — for routing:
mercury inception labs 1109 tokens per second 737 tokens per second
parallel refinement not sequential prediction noisy simultaneously
copilot arena fastest model second quality throughput H100
mercury coder mini small diffusion LLM commercial scale
