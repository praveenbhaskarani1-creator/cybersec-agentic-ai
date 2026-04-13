-- Aurora PostgreSQL initialization script

-- Step 1: Enable pgvector extension
-- CREATE EXTENSION IF NOT EXISTS vector;

-- Step 2: Create ot_events table
-- Step 3: Create asset_inventory table
-- Step 4: Create cve_records table
-- Step 5: Create threat_groups table
-- Step 6: Create rag_chunks table with vector(1536) column + ivfflat index
-- Step 7: Create anomaly_alerts table
-- Step 8: Create approval_queue table
-- Step 9: Create users table
-- Step 10: Create audit_log table
-- Step 11: Create indexes on commonly queried columns (asset_id, cve_id, timestamp)
-- Step 12: Create RBAC roles (analyst_role, admin_role, readonly_role)
