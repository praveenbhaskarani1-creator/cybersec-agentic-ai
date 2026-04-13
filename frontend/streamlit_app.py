# Streamlit Dashboard — Analyst/SOC Interface (runs on EC2)

# Step 1: Configure page title, icon, layout (wide mode)
# Step 2: Add sidebar — user login (JWT token input or SSO), role display
# Step 3: Main panel — natural language query input box
# Step 4: On submit — POST to FastAPI /ask endpoint with question + JWT token
# Step 5: Display answer with source citations and detected intent
# Step 6: If hil_required=True — show "Pending Analyst Approval" status indicator
# Step 7: Approval panel — fetch /approval queue, display pending decisions
#         - Analyst can approve or reject with notes
#         - POST decision to /approval endpoint
# Step 8: Audit log panel — fetch /audit logs, display as sortable table
# Step 9: Anomaly alerts panel — show active alerts from API
# Step 10: Auto-refresh every N seconds for real-time updates
