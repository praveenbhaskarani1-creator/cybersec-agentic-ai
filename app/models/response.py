# Pydantic response schemas

# AskResponse:
#   - answer: str — final generated answer
#   - sources: list[str] — RAG source documents used
#   - intent: str — detected intent
#   - hil_required: bool — whether analyst approval is pending

# ApprovalQueueItem:
#   - queue_id: str
#   - agent_output: dict
#   - status: str
#   - created_at: datetime

# AuditLogEntry:
#   - user_id: str
#   - action: str
#   - intent: str
#   - timestamp: datetime
#   - outcome: str
