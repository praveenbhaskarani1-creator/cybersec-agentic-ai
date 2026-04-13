# SQLAlchemy ORM Models — Aurora PostgreSQL + pgvector

# Table: ot_events
#   — id, protocol, severity, anomaly_score, timestamp, asset_id, raw_payload

# Table: asset_inventory
#   — id, vendor, firmware_version, firmware_age_days, cores, site, cves (array), risk_score

# Table: cve_records
#   — cve_id, cvss_score, cvss_vector, patch_status, exposed_assets (array), published_date, description

# Table: threat_groups
#   — id, name (VOLT/TYPHOON etc.), ttps (array), iocs (array), sectors (array), last_seen

# Table: rag_chunks
#   — id, content, embedding (vector 1536), source, doc_type, metadata (jsonb), created_at

# Table: anomaly_alerts
#   — id, asset_id, issue, severity, status, detected_at, resolved_at

# Table: approval_queue
#   — id, agent_output (jsonb), hil_status, analyst_id, decision, created_at, decided_at

# Table: users
#   — id, username, role (analyst/admin/readonly), jwt_sub, created_at

# Table: audit_log
#   — id, user_id, action, intent, question, answer_summary, hil_status, timestamp
