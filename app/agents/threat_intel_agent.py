# Threat Intel Agent — handles IOCs, TTPs, threat group queries

# Step 1: Receive AgentState with intent="threat_intel"
# Step 2: Call RAG retriever to fetch relevant threat intel chunks from pgvector
# Step 3: Call mcp-threat-intel tool (VirusTotal API, IOC lookups, TTP mappings)
# Step 4: Combine RAG context + MCP results into prompt
# Step 5: Call AWS Bedrock for final answer generation
# Step 6: Populate AgentState.answer and AgentState.sources
# Step 7: Route to HIL node if confidence is low or sensitive action required
