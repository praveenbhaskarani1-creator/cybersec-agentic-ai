# LangGraph StateGraph — Agentic Core

# Step 1: Import LangGraph StateGraph, START, END
# Step 2: Import all agent nodes (threat_intel, asset_risk, vuln_scoring, compliance, incident_resp)
# Step 3: Import supervisor node (intent router)
# Step 4: Import HIL approval node
# Step 5: Import audit logger node
# Step 6: Define StateGraph with AgentState
# Step 7: Add nodes — supervisor, each agent, hil_node, audit_logger
# Step 8: Add conditional edges from supervisor → correct agent based on intent
# Step 9: Add HIL interrupt edge — agent output → hil_node → resume or reject
# Step 10: Add audit_logger as final node before END
# Step 11: Compile graph
# Step 12: Define async run_graph(question, user_id) entry point
