# Tests — Ingestion pipeline

# test_nvd_fetch_returns_cves: ICS-CERT/NVD fetch → list of CVE dicts
# test_cve_upsert_no_duplicates: insert same CVE twice → only one record in DB
# test_mitre_fetch_returns_techniques: MITRE ATT&CK fetch → list of technique dicts
# test_threat_group_upsert: insert threat group → threat_groups table updated
# test_ingestion_generates_embeddings: after ingestion → rag_chunks has new rows with vectors
