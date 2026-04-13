# Human-in-the-Loop (HIL) Approval Node

# Step 1: On entry, write agent_output to approval_queue table (DB) with status="pending"
# Step 2: Trigger LangGraph interrupt — pause execution and wait for analyst decision
# Step 3: Expose approval_queue via /approval API endpoint (see main.py)
# Step 4: On analyst approval — resume graph, set hil_status="approved", continue to audit_logger
# Step 5: On analyst rejection — set hil_status="rejected", return rejection message, skip to audit_logger
# Step 6: Timeout handling — if no decision within N minutes, auto-escalate
