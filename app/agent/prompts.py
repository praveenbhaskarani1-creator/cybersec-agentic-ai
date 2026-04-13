# Centralized prompt templates for all agents and supervisor

# SUPERVISOR_INTENT_PROMPT — classify query into one of 5 intents
# THREAT_INTEL_PROMPT — answer threat intel questions using IOCs, TTPs, RAG context
# ASSET_RISK_PROMPT — assess OT/ICS asset risk using inventory and firmware data
# VULN_SCORING_PROMPT — score CVEs, suggest patches, prioritize by CVSS
# COMPLIANCE_PROMPT — check against NERC CIF / IEC 62443 controls
# INCIDENT_RESP_PROMPT — recommend playbook steps and advisories for incident
# RAG_CONTEXT_TEMPLATE — inject retrieved chunks into agent prompts
