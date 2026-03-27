# Agent Skill: DATABASE

SKILL: database
KEYWORDS: SQL query database select insert update delete schema table join
TYPE: capability

DESCRIPTION:
This skill enables agents to perform database operations.
When a query requires database the agent activates this skill.
Document bytes encode the database knowledge pattern.

QUERY_TRIGGERS: SQL query database select insert update delete schema table join

USAGE:
Agent reads this skill doc via RLM when database is needed.
Diffusion over skill bytes produces database outputs.
No external API required — document IS the skill implementation knowledge.
