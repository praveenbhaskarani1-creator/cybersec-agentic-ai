# Tests — FastAPI endpoints

# test_health_returns_ok: GET /health → 200
# test_ask_unauthorized: POST /ask without token → 401
# test_ask_with_valid_jwt: POST /ask with analyst token → 200 with answer
# test_ask_readonly_rejected: POST /ask with readonly token → 403
# test_approval_requires_analyst: POST /approval with readonly → 403
# test_audit_requires_admin: GET /audit with analyst → 403
