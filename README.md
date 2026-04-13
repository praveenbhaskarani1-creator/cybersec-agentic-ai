# Cybersec Agentic AI System

An OT/ICS cybersecurity agentic AI platform built with LangGraph, FastAPI, AWS Bedrock, and PostgreSQL + pgvector. Enables SOC analysts to query threat intelligence, asset risk, vulnerabilities, compliance posture, and incident response playbooks via natural language.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit (EC2) |
| API | FastAPI + JWT RBAC |
| Agentic Core | LangGraph (ECS Fargate) |
| LLM | AWS Bedrock (TitanHaiku) |
| Embeddings | AWS Bedrock Titan Embed |
| Vector DB | Aurora PostgreSQL + pgvector |
| Message Queue | Apache Kafka |
| Infra | AWS ECS Fargate, EC2, Aurora RDS, CloudWatch, S3 |

---

## Architecture

```mermaid
flowchart TD
    User(["Analyst / SOC"])
    User -->|Natural language query| SD["Streamlit Dashboard - EC2"]
    SD -->|HTTP / REST| FB

    subgraph AGENTIC [AGENTIC CORE - ECS Fargate - LangGraph]
        direction TB
        FB["FastAPI Backend"]
        FB --> RBAC["RBAC Middleware - JWT Auth"]
        RBAC --> SUP{"Supervisor Agent\nIntent Router"}

        SUP -->|threat_intel| TIA["Threat Intel Agent"]
        SUP -->|asset_risk| ARA["Asset Risk Agent"]
        SUP -->|vuln_scoring| VSA["Vuln Scoring Agent"]
        SUP -->|compliance| CA["Compliance Agent"]
        SUP -->|incident_resp| IRA["Incident Resp Agent"]

        TIA --- MCP1["mcp-threat-intel\nVirusTotal, IOCs, TTPs"]
        ARA --- MCP2["mcp-ot-assets\nInventory, Firmware, Cores"]
        VSA --- MCP3["mcp-vuln-mgmt\nCVE, CVSS, Patch Status"]
        CA  --- MCP4["mcp-compliance\nNERC CIF, IEC 62443"]
        IRA --- MCP5["mcp-cap-search\nPlaybooks, Advisories"]

        TIA & ARA & VSA & CA & IRA --> RAG["RAG Retrieval Layer\npgvector cosine + cross-encoder re-rank"]
        RAG --> HIL["HIL Approval Node\nLangGraph interrupt - analyst review - resume"]
        HIL --> AUDIT["Audit Logger"]
    end

    subgraph INGESTION [INGESTION PIPELINE - Edge Collectors + Kafka + Python Workers]
        direction LR
        I1["Modbus / DNP3 / OPC-UA"]
        I2["Syslog / PCAP / SCADA"]
        I3["ICS-CERT / NVD Feeds"]
        I4["MITRE ATT&CK ICS"]
        I5["Worldview / ISAC"]
    end

    subgraph DATA [DATA LAYER - Aurora PostgreSQL + pgvector - AWS RDS]
        direction LR
        D1[("ot_events")]
        D2[("asset_inventory")]
        D3[("cve_records")]
        D4[("threat_groups")]
        D5[("rag_chunks\nvector-1536")]
        D6[("anomaly_alerts")]
        D7[("approval_queue")]
        D8[("audit_log")]
    end

    subgraph DEPLOY [DEPLOYMENT - AWS]
        direction LR
        AWS1["ECS Fargate"]
        AWS2["EC2 Streamlit"]
        AWS3["Aurora RDS"]
        AWS4["Bedrock TitanHaiku"]
        AWS5["CloudWatch / S3"]
    end

    INGESTION -->|Kafka topics| DATA
    AGENTIC <-->|SQLAlchemy / pgvector| DATA
    AGENTIC -.->|LLM calls| AWS4

    style AGENTIC   fill:#f0f4ff,stroke:#5c7cfa,stroke-width:2px
    style DATA      fill:#fff8e1,stroke:#f59f00,stroke-width:2px
    style INGESTION fill:#e6fcf5,stroke:#20c997,stroke-width:2px
    style DEPLOY    fill:#fff0f6,stroke:#e64980,stroke-width:2px
    style SUP       fill:#d0ebff,stroke:#1971c2
    style RAG       fill:#d3f9d8,stroke:#2f9e44
    style HIL       fill:#ffe8cc,stroke:#e67700
    style AUDIT     fill:#f3f0ff,stroke:#7048e8
```

---

## Project Structure

```
cybersec-agentic-ai/
├── app/
│   ├── main.py                    # FastAPI entrypoint
│   ├── config.py                  # Pydantic settings
│   ├── middleware/rbac.py         # JWT Auth + RBAC
│   ├── agent/                     # LangGraph graph, state, supervisor, HIL, audit
│   ├── agents/                    # 5 specialist agents
│   ├── mcp/                       # 5 MCP tool servers
│   ├── rag/                       # Retriever, reranker, embeddings
│   ├── db/                        # PostgreSQL connection + ORM models
│   └── models/                    # Request/response schemas
├── ingestion/                     # Edge collectors + Kafka workers
├── frontend/streamlit_app.py      # SOC Dashboard
├── infra/                         # ECS task def, RDS init SQL, CloudWatch Terraform
├── tests/                         # pytest test suites
├── .env.example                   # Environment variable template
├── requirements.txt
└── .gitignore
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-org/cybersec-agentic-ai.git
cd cybersec-agentic-ai

# 2. Set up environment
cp .env.example .env
# Fill in AWS credentials, DB connection, API keys

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize the database
psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB -f infra/rds/init.sql

# 5. Run ingestion pipeline (one-time seed)
python -m ingestion.mitre_attack_ics
python -m ingestion.ics_cert_nvd

# 6. Start the API
uvicorn app.main:app --host 0.0.0.0 --port 8000

# 7. Start the frontend
streamlit run frontend/streamlit_app.py
```

---

## Agents

| Agent | Intent | MCP Tool | Data Source |
|---|---|---|---|
| Threat Intel Agent | `threat_intel` | mcp-threat-intel | VirusTotal, IOC DB, TTPs |
| Asset Risk Agent | `asset_risk` | mcp-ot-assets | asset_inventory, firmware DB |
| Vuln Scoring Agent | `vuln_scoring` | mcp-vuln-mgmt | cve_records, NVD |
| Compliance Agent | `compliance` | mcp-compliance | NERC CIF, IEC 62443 |
| Incident Resp Agent | `incident_resp` | mcp-cap-search | Playbooks, CISA advisories |

---

## Key Features

- **Natural Language Queries** — SOC analysts query in plain English
- **Supervisor Intent Routing** — LangGraph routes to the correct specialist agent
- **RAG with Re-ranking** — pgvector cosine search + cross-encoder for precision
- **Human-in-the-Loop** — LangGraph interrupt for analyst approval before sensitive actions
- **RBAC** — JWT-based role enforcement (analyst / admin / readonly)
- **Full Audit Trail** — every action logged to audit_log table
- **Real-time Ingestion** — Kafka-based pipeline from OT edge devices and threat feeds

---

## License

MIT
