# Incident Response Agent — playbook lookup and advisory search

# Step 1: Receive AgentState with intent="incident_resp"
# Step 2: Call mcp-cap-search to search playbooks and advisories by incident type
# Step 3: Query anomaly_alerts table for active alerts matching the incident
# Step 4: Call RAG retriever for MITRE ATT&CK ICS technique mitigations
# Step 5: Call AWS Bedrock to generate step-by-step incident response plan
# Step 6: Populate AgentState.answer with playbook steps and containment actions
# Step 7: Route to HIL node — all incident response actions require analyst approval
