# Ingestion — Modbus / DNP3 / OPC-UA Edge Collector

# Step 1: Connect to OT edge devices via Modbus TCP, DNP3, or OPC-UA protocol
# Step 2: Poll device registers/data points at configured intervals
# Step 3: Parse raw protocol frames into structured event dicts
# Step 4: Enrich with asset metadata (lookup asset_inventory by device IP/ID)
# Step 5: Compute anomaly_score using basic threshold rules
# Step 6: Publish structured event to Kafka topic: ot_events_raw
# Step 7: Worker consumes Kafka topic and inserts into ot_events table (PostgreSQL)
