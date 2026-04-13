# Ingestion — Worldview / ISAC Threat Intelligence Feed

# Step 1: Authenticate with Worldview API or ISAC portal (E-ISAC, WaterISAC, etc.)
# Step 2: Fetch latest threat intelligence reports and IOC feeds
# Step 3: Parse reports — extract threat actors, IOCs, affected sectors, TTPs
# Step 4: Upsert into threat_groups table with IOC and sector arrays
# Step 5: Generate embeddings for report text and upsert into rag_chunks table
# Step 6: Cross-reference new IOCs against ot_events table for active matches
# Step 7: Trigger anomaly_alerts if active IOC match found in recent events
