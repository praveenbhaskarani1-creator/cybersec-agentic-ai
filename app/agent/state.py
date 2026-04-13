# AgentState — shared state across all LangGraph nodes

# Step 1: Define AgentState as TypedDict
# Step 2: Fields:
#   - question: str — original user query
#   - user_id: str — for RBAC and audit
#   - intent: str — detected intent from supervisor
#   - agent_output: dict — result from the selected agent
#   - rag_context: list[str] — retrieved chunks from pgvector
#   - sources: list[str] — source documents for answer
#   - answer: str — final answer to return
#   - hil_status: str — "pending" | "approved" | "rejected"
#   - audit_logged: bool — whether audit entry was written
#   - error: str | None — any error message
