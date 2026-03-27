# Agent Skill: REASONING

SKILL: reasoning
KEYWORDS: think analyze reason infer conclude evidence hypothesis proof
TYPE: capability

DESCRIPTION:
This skill enables agents to perform reasoning operations.
When a query requires reasoning the agent activates this skill.
Document bytes encode the reasoning knowledge pattern.

QUERY_TRIGGERS: think analyze reason infer conclude evidence hypothesis proof

USAGE:
Agent reads this skill doc via RLM when reasoning is needed.
Diffusion over skill bytes produces reasoning outputs.
No external API required — document IS the skill implementation knowledge.
