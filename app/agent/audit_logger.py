# Audit Logger Node — writes every interaction to audit_log table

# Step 1: Extract from AgentState: user_id, question, intent, answer, hil_status
# Step 2: Write record to users/audit_log table with: who, what (action), when (timestamp), outcome
# Step 3: If hil_status == "rejected", flag the record for compliance review
# Step 4: Set AgentState.audit_logged = True
# Step 5: Forward to END node
