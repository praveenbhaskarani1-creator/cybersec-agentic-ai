# Supervisor Agent — Intent Router

# Step 1: Load intent classification prompt from prompts.py
# Step 2: Call AWS Bedrock (TitanHaiku) with user question to detect intent
# Step 3: Map intent to one of: threat_intel | asset_risk | vuln_scoring | compliance | incident_resp
# Step 4: Update AgentState with detected intent
# Step 5: Return routing decision for LangGraph conditional edges
