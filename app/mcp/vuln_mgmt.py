# MCP Tool Server — Vulnerability Management
# Connects to: cve_records table, NVD API, ICS-CERT feeds

# Step 1: Define MCP tool schema
# Step 2: Implement get_cve(cve_id) — fetch CVE details from cve_records or NVD API
# Step 3: Implement get_cvss_score(cve_id) — return CVSS v3 base score and vector
# Step 4: Implement get_patch_status(cve_id, asset_id) — check if patch is available/applied
# Step 5: Implement list_exposed_assets(cve_id) — find all assets exposed to this CVE
# Step 6: Return prioritized vuln data (score, exploitability, patch availability)
