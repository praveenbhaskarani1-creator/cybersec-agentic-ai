# Vulnerability Scoring Agent — CVE scoring, patch prioritization

# Step 1: Receive AgentState with intent="vuln_scoring"
# Step 2: Call mcp-vuln-mgmt to fetch CVE details, CVSS scores, patch status
# Step 3: Query cve_records table for exposed assets with matching CVEs
# Step 4: Prioritize vulnerabilities by CVSS score and asset criticality
# Step 5: Call RAG retriever for NVD/ICS-CERT advisories on the CVE
# Step 6: Call AWS Bedrock to generate patching recommendations
# Step 7: Populate AgentState.answer with prioritized vuln list + patch plan
