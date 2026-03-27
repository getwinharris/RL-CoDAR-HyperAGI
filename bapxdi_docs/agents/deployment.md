# Agent Skill: DEPLOYMENT

SKILL: deployment
KEYWORDS: deploy docker kubernetes container orchestration cloud AWS GCP Azure
TYPE: capability

DESCRIPTION:
This skill enables agents to perform deployment operations.
When a query requires deployment the agent activates this skill.
Document bytes encode the deployment knowledge pattern.

QUERY_TRIGGERS: deploy docker kubernetes container orchestration cloud AWS GCP Azure

USAGE:
Agent reads this skill doc via RLM when deployment is needed.
Diffusion over skill bytes produces deployment outputs.
No external API required — document IS the skill implementation knowledge.
