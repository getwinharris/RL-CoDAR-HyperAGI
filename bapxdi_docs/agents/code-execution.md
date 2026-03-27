# Agent Skill: CODE-EXECUTION

SKILL: code-execution
KEYWORDS: run execute python javascript bash shell command terminal subprocess
TYPE: capability

DESCRIPTION:
This skill enables agents to perform code execution operations.
When a query requires code execution the agent activates this skill.
Document bytes encode the code execution knowledge pattern.

QUERY_TRIGGERS: run execute python javascript bash shell command terminal subprocess

USAGE:
Agent reads this skill doc via RLM when code execution is needed.
Diffusion over skill bytes produces code execution outputs.
No external API required — document IS the skill implementation knowledge.
