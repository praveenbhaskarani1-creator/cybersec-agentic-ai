# MCP Tool Server — CAP/Playbook Search
# Connects to: playbooks store, advisories database

# Step 1: Define MCP tool schema
# Step 2: Implement search_playbook(incident_type) — find matching IR playbook
# Step 3: Implement get_playbook_steps(playbook_id) — return ordered response steps
# Step 4: Implement search_advisories(keyword) — search ICS-CERT/CISA advisories
# Step 5: Implement get_advisory(advisory_id) — fetch full advisory details
# Step 6: Return playbook steps and advisory links with relevance scores
