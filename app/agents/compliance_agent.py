# Compliance Agent — NERC CIF and IEC 62443 compliance checks

# Step 1: Receive AgentState with intent="compliance"
# Step 2: Call mcp-compliance to fetch relevant NERC CIF / IEC 62443 controls
# Step 3: Query asset_inventory and ot_events for compliance-relevant data
# Step 4: Call RAG retriever for compliance documentation and control mappings
# Step 5: Evaluate current posture against required controls
# Step 6: Call AWS Bedrock to generate compliance gap analysis report
# Step 7: Populate AgentState.answer with gaps, severity, and remediation steps
# Step 8: Always route to HIL node (compliance actions require analyst approval)
