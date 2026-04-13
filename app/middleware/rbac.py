# RBAC Middleware — JWT Auth + Role-Based Access Control

# Step 1: Extract Bearer token from Authorization header
# Step 2: Verify JWT signature using secret from config.py
# Step 3: Decode claims — user_id, role, expiry
# Step 4: Enforce role permissions per endpoint:
#         - /ask         → analyst, admin
#         - /approval    → analyst, admin
#         - /audit       → admin only
#         - /health      → public
# Step 5: Reject unauthorized requests with 401/403
# Step 6: Attach user context to request state for downstream use
