# WHAT IS BMAD

BMAD stands for Breakthrough Method of Agile AI-Driven Development.
Created by: bmad-code-org. GitHub: github.com/bmad-code-org/BMAD-METHOD

THE CORE IDEA:
Traditional AI: one model, one persona, answers everything the same way.
BMAD: many personas, each defined as a markdown document.
Each persona IS its document. The document IS the agent.

HOW IT WORKS:
architect.md contains how an architect thinks about system design.
qa-engineer.md contains how a QA thinks about testing.
product-manager.md contains how a PM thinks about requirements.
When a query arrives the model reads the relevant persona doc.
The persona doc bytes condition the diffusion output.
Output sounds like that persona because those bytes are the signal.

WHY THIS MATTERS FOR BAPXDI:
bapXdi already does this — docs are the model.
BMAD formalizes it: structured personas, structured workflows, structured skills.
Persona selection IS an NLP task — language reads the query, picks the persona doc.
That selection uses diffusion the same way all generation uses diffusion.

SKILLS VS KNOWLEDGE:
Knowledge docs (Wikipedia, NuminaMath) = the model knows facts.
Skill docs (web-search.md, code-execution.md) = the model knows HOW to act.
Persona docs (architect.md, developer.md) = the model knows WHO to be.
Without skills the model can only talk. With skills it can work.

THE FOUR PHASES:
1. Analysis:      query arrives → language identifies intent → persona selected
2. Planning:      persona reads relevant skill docs → plan crystallized
3. Solutioning:   skill docs + knowledge docs → solution diffused
4. Implementation: output crystallized → evolver watches → docs updated

PARTY MODE:
Multiple personas activated simultaneously.
Each reads its own document shard via parallel RLM hops.
Language assembles all crystallized outputs.
Same as Mercury 2 parallel generation but across personas.
