# BMAD METHOD — bapXdi Adaptation

Breakthrough Method of Agile AI-Driven Development adapted for bapXdi.
Source: github.com/bmad-code-org/BMAD-METHOD

bapXdi replaces the "AI chatbot" in BMAD with byte-diffusion over documents.
Agents don't have fixed prompts — they have document shards as their brain.
Each agent persona = a docs/ subfolder of domain knowledge bytes.

## Four-Phase Workflow

1. **Analysis** — Capture requirements → `queries.json` turn with attachments
2. **Planning** — Break into user stories → RLM hops across planning docs
3. **Solutioning** — Architecture design → diffuse over architecture docs
4. **Implementation** — Code generation → diffuse over package brain docs

## Agent Personas (21 total)

Each agent = a set of document shards it preferentially reads via RLM.
Language routes query to the agent. Agent's docs are its weights.
