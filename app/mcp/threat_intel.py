# MCP Tool Server — Threat Intel
# Connects to: VirusTotal API, IOC feeds, TTP databases

# Step 1: Define MCP tool schema (name, description, input/output types)
# Step 2: Implement lookup_ioc(indicator) — query VirusTotal for IP/hash/domain
# Step 3: Implement get_ttps(threat_group) — fetch TTPs for a known threat group
# Step 4: Implement search_iocs(keyword) — search IOC database by keyword
# Step 5: Return structured results (threat score, context, source)
# Step 6: Handle API rate limits and errors gracefully
