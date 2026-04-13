# Ingestion — ICS-CERT / NVD Feed Ingestion

# Step 1: Poll ICS-CERT RSS/API for new advisories (scheduled, e.g. every 6h)
# Step 2: Poll NVD API for new CVEs relevant to OT/ICS products
# Step 3: Parse advisory/CVE data — extract CVE IDs, CVSS scores, affected products
# Step 4: Match affected products against asset_inventory to flag exposed assets
# Step 5: Upsert into cve_records table (avoid duplicates using CVE ID as key)
# Step 6: Generate embeddings for advisory text and upsert into rag_chunks table
# Step 7: Trigger anomaly_alerts for critical CVEs (CVSS >= 9.0) on exposed assets
