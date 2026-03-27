# Agent Skill: MEMORY

SKILL: memory
KEYWORDS: store retrieve context history session state persist cache
TYPE: capability

DESCRIPTION:
This skill enables agents to perform memory operations.
When a query requires memory the agent activates this skill.
Document bytes encode the memory knowledge pattern.

QUERY_TRIGGERS: store retrieve context history session state persist cache

USAGE:
Agent reads this skill doc via RLM when memory is needed.
Diffusion over skill bytes produces memory outputs.
No external API required — document IS the skill implementation knowledge.
