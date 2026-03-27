# Agent Skill: PLANNING

SKILL: planning
KEYWORDS: plan steps breakdown task decompose schedule timeline milestone
TYPE: capability

DESCRIPTION:
This skill enables agents to perform planning operations.
When a query requires planning the agent activates this skill.
Document bytes encode the planning knowledge pattern.

QUERY_TRIGGERS: plan steps breakdown task decompose schedule timeline milestone

USAGE:
Agent reads this skill doc via RLM when planning is needed.
Diffusion over skill bytes produces planning outputs.
No external API required — document IS the skill implementation knowledge.
