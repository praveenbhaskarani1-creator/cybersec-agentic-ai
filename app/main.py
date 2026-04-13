# FastAPI entrypoint for Cybersec Agentic AI System

# Step 1: Initialize FastAPI app with title and version
# Step 2: Add CORS middleware
# Step 3: Register RBAC JWT middleware
# Step 4: Import and include API routers
# Step 5: Define /health endpoint
# Step 6: Define /ask endpoint — accepts AskRequest, runs LangGraph, returns AskResponse
# Step 7: Define /approval endpoint — analyst reviews HIL queue and approves/rejects
# Step 8: Define /audit endpoint — fetch audit logs for SOC dashboard
