# Agent Skill: MONITORING

SKILL: monitoring
KEYWORDS: log metrics alert dashboard Grafana Prometheus trace observability
TYPE: capability

DESCRIPTION:
This skill enables agents to perform monitoring operations.
When a query requires monitoring the agent activates this skill.
Document bytes encode the monitoring knowledge pattern.

QUERY_TRIGGERS: log metrics alert dashboard Grafana Prometheus trace observability

USAGE:
Agent reads this skill doc via RLM when monitoring is needed.
Diffusion over skill bytes produces monitoring outputs.
No external API required — document IS the skill implementation knowledge.
