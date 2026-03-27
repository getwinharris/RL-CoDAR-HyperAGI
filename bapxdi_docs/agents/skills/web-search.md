# Agent Skill: WEB-SEARCH

SKILL: web-search
KEYWORDS: search internet browse URL fetch HTTP request scrape extract content
TYPE: capability

DESCRIPTION:
This skill enables agents to perform web search operations.
When a query requires web search the agent activates this skill.
Document bytes encode the web search knowledge pattern.

QUERY_TRIGGERS: search internet browse URL fetch HTTP request scrape extract content

USAGE:
Agent reads this skill doc via RLM when web search is needed.
Diffusion over skill bytes produces web search outputs.
No external API required — document IS the skill implementation knowledge.
