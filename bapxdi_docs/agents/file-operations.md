# Agent Skill: FILE-OPERATIONS

SKILL: file-operations
KEYWORDS: read write create delete move copy file directory path filesystem
TYPE: capability

DESCRIPTION:
This skill enables agents to perform file operations operations.
When a query requires file operations the agent activates this skill.
Document bytes encode the file operations knowledge pattern.

QUERY_TRIGGERS: read write create delete move copy file directory path filesystem

USAGE:
Agent reads this skill doc via RLM when file operations is needed.
Diffusion over skill bytes produces file operations outputs.
No external API required — document IS the skill implementation knowledge.
