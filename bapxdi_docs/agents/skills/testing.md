# Agent Skill: TESTING

SKILL: testing
KEYWORDS: test unittest pytest assert mock fixture coverage report pass fail
TYPE: capability

DESCRIPTION:
This skill enables agents to perform testing operations.
When a query requires testing the agent activates this skill.
Document bytes encode the testing knowledge pattern.

QUERY_TRIGGERS: test unittest pytest assert mock fixture coverage report pass fail

USAGE:
Agent reads this skill doc via RLM when testing is needed.
Diffusion over skill bytes produces testing outputs.
No external API required — document IS the skill implementation knowledge.
