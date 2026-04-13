# Ingestion — MITRE ATT&CK ICS Framework Ingestion

# Step 1: Fetch MITRE ATT&CK ICS STIX bundle from official repo/API
# Step 2: Parse techniques, sub-techniques, mitigations, and threat group mappings
# Step 3: Extract TTPs per threat group and map to STIX relationship objects
# Step 4: Upsert threat_groups table with TTP arrays and IOC associations
# Step 5: Generate embeddings for technique descriptions and mitigations
# Step 6: Upsert into rag_chunks table with doc_type="mitre_attack_ics"
# Step 7: Schedule refresh weekly (MITRE updates quarterly)
