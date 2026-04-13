# Pydantic request schemas

# AskRequest:
#   - question: str — natural language query from analyst
#   - user_id: str — from JWT (injected by RBAC middleware)

# ApprovalRequest:
#   - queue_id: str — approval_queue record ID
#   - decision: Literal["approved", "rejected"]
#   - analyst_notes: str | None
