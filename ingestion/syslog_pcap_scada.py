# Ingestion — Syslog / PCAP / SCADA Collector

# Step 1: Listen for syslog UDP/TCP messages from SCADA systems and network devices
# Step 2: Capture PCAP traffic on OT network segments for deep packet inspection
# Step 3: Parse syslog messages — extract severity, facility, host, message
# Step 4: Parse PCAP frames — identify OT protocols (Modbus, EtherNet/IP, PROFINET)
# Step 5: Detect anomalies — unexpected commands, out-of-range values, unknown hosts
# Step 6: Publish to Kafka topic: syslog_events_raw and pcap_events_raw
# Step 7: Worker inserts into ot_events and anomaly_alerts tables
