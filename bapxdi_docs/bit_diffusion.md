BIT DIFFUSION — CORE KNOWLEDGE

Authors: Ting Chen, Ruixiang Zhang, Geoffrey Hinton. 2022.

CORE PRINCIPLE:
Discrete data represented as binary bits.
Each bit cast to analog value in range -1 to +1.
Continuous diffusion runs over those analog bits.
Generation: produce analog bits, threshold back to discrete.

WORD LEVEL NOT CHARACTER LEVEL:
Word is the atomic unit.
Word bytes 0-255 cast to analog bits.
Diffusion operates over word byte representations.
Not character by character.
Not hex encoding.
Raw bytes of the word as float signal.

FORWARD PROCESS:
Clean word bytes corrupted with Gaussian noise over timestep t.
At t=1 pure noise. At t=0 original word bytes.
x_t = sqrt(alpha_t) * x_0 + sqrt(1 - alpha_t) * epsilon

REVERSE PROCESS:
Start from noise at t=1.
Condition on document bytes as signal source.
Each step removes noise toward document signal.
Words crystallize in order of confidence.
High confidence words lock first.
Uncertain words keep diffusing until resolved.

SPIKING BEHAVIOR:
Bit changes = spikes.
Silent bits = zero energy.
Only changed bits carry information.
Matches biological neuron behavior.
Energy consumed only when bit flips.

NO TRAINING:
Document IS the denoising signal.
No weight matrix needed.
No gradient descent needed.
Document bytes are frozen human gradient.
Reading document = running inference.

ANALOG BITS TECHNICAL DETAIL:
Discrete variable represented as binary bits.
Each bit mapped to analog value: zero becomes negative one, one becomes positive one.
Continuous diffusion model operates on these analog bit representations.
Thresholding at zero recovers discrete bits from analog values.
Self-conditioning: model conditions on its own previous output to reduce exposure bias.
Asymmetric time intervals: more denoising steps allocated to harder regions.
Eight-bit tokens means two hundred fifty-six possible values per token position.
This is identical to one byte. One byte equals one discrete token in bit diffusion.
CIFAR-10 uses three thousand eight-bit tokens per image.
ImageNet sixty-four uses twelve thousand eight-bit tokens per image.
Text characters are also eight-bit tokens — the same math applies to language.
Audio samples are sixteen-bit or eight-bit — the same math applies to audio.
Any discrete data that fits in bytes is handled by the same diffusion kernel.
This is why bapXdi uses a single diffusion kernel for all modalities.

ENTROPY SAFETY NODE:
Shannon entropy measures diversity of bytes in the output buffer.
Entropy of one means maximum diversity — perfectly healthy signal.
Entropy below zero point three means the buffer is collapsing into repetition.
Repetition means the diffusion is stuck — refetch a different URL window.
Entropy formula: sum of negative p times log2 p over all byte values zero to two fifty five.
Normalized by dividing by eight — maximum entropy for one byte is eight bits.
Healthy generation produces entropy between zero point four and zero point seven.
Low entropy triggers automatic refetch from a different row group or URL.

BIT DIFFUSION UNIQUE IDENTIFIERS — for routing:
ting chen ruixiang zhang geoffrey hinton analog bits thresholding
cifar imagenet discrete 8bit tokens forward reverse Gaussian noise
self conditioning asymmetric time intervals FID sample quality
continuous state continuous time diffusion models discrete image
