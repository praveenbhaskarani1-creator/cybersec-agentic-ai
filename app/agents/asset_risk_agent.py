# Asset Risk Agent — handles OT/ICS asset inventory and risk scoring

# Step 1: Receive AgentState with intent="asset_risk"
# Step 2: Call mcp-ot-assets to fetch asset inventory (vendor, firmware, cores)
# Step 3: Query asset_inventory table in PostgreSQL for asset details
# Step 4: Compute risk score based on firmware age, known CVEs, exposure
# Step 5: Call RAG retriever for relevant asset risk documentation
# Step 6: Call AWS Bedrock to generate risk summary and recommendations
# Step 7: Populate AgentState.answer with risk score + remediation steps
