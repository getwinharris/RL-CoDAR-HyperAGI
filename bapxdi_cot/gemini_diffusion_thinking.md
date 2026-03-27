GEMINI DIFFUSION — ACTUAL FACTS
Source: deepmind.google/models/gemini-diffusion
Google I/O May 20 2025. No arxiv paper. Experimental model.

WHAT IT ACTUALLY DOES (from official DeepMind page and confirmed reports):
Generates entire blocks of tokens at once — not one token at a time.
Refines noise step-by-step — starts from random noise, crystallizes to text.
Generates content significantly faster than autoregressive models.
Corrects errors during generation — self-correction inside the block.
1479 tokens per second. Up to 2000 tokens/sec on code tasks.
Responds more coherently than autoregressive models because it sees full context.

KEY PRINCIPLE FOR BAPXDI:
The block starts as noise. All positions in the block refine simultaneously.
Self-correction happens mid-generation — wrong words get wiped and re-denoised.
This is NOT left-to-right. The whole block is alive at once.
In bapXdi: the signal_words block from RLM all start as byte-level noise.
All positions denoise toward doc signal bytes simultaneously.
At halfway point (step 6 of 12): positions far from signal re-noise and re-denoise.
This implements the self-correction Gemini Diffusion describes.

WHAT WE TAKE FROM THIS:
Block-level generation — entire answer block starts noisy together.
Self-correction at midpoint — re-noise uncertain positions.
Parallel refinement — all positions update every step.
Doc bytes are the signal — no trained denoising network needed.

WHAT WE DO NOT TAKE:
Gemini Diffusion still uses a trained transformer as the denoiser.
bapXdi removes the trained transformer entirely.
Document bytes from HF datasets replace the trained denoiser.
RLM peeks the right doc bytes. Diffusion crystallizes from those bytes.
No training. No weights. Docs are the model.

GEMINI DIFFUSION UNIQUE IDENTIFIERS:
gemini block diffusion sixteen steps 128 words per block self correction
google deepmind IO May 2025 1479 tokens per second faster mercury
entire blocks tokens once refining noise stepbystep not left right
corrects errors during generation within block all positions noisy
