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

> Three diagrams covering: (1) Agentic Core Flow, (2) RAG + Data Pipeline, (3) AWS Deployment

---

### Diagram 1 — Agentic Core Flow

```mermaid
flowchart TD
    User((User))
    User -->|Natural Language| SD[Streamlit Dashboard]
    SD -->|API Request| FB

    subgraph CORE [Agentic Core - LangGraph on ECS Fargate]
        FB[FastAPI Backend]
        FB --> RBAC[RBAC Middleware - JWT Auth]
        RBAC --> SUP{Supervisor Agent}

        SUP -->|Intents| TIA[Threat Intel Agent]
        SUP -->|Intents| ARA[Asset Risk Agent]
        SUP -->|Intents| VSA[Vuln Scoring Agent]
        SUP -->|Intents| CA[Compliance Agent]
        SUP -->|Intents| IRA[Incident Resp Agent]

        TIA -->|Tool Calling| MCP1[mcp-threat-intel\nVirusTotal - IOCs - TTPs]
        ARA -->|Tool Calling| MCP2[mcp-ot-assets\nInventory - Firmware - Cores]
        VSA -->|Tool Calling| MCP3[mcp-vuln-mgmt\nCVE - CVSS - Patch Status]
        CA  -->|Tool Calling| MCP4[mcp-compliance\nNERC CIF - IEC 62443]
        IRA -->|Tool Calling| MCP5[mcp-cap-search\nPlaybooks - Advisories]
    end

    MCP1 -->|RAG + LLM| OUT[RAG + HIL + Audit Layer]
    MCP2 -->|RAG + LLM| OUT
    MCP3 -->|RAG + LLM| OUT
    MCP4 -->|RAG + LLM| OUT
    MCP5 -->|RAG + LLM| OUT

    style CORE fill:#fafafa,stroke:#5c7cfa,stroke-width:2px
    style SUP  fill:#d0ebff,stroke:#1971c2
```

---

### Diagram 2 — RAG, HIL and Data Pipeline

```mermaid
flowchart TD
    IN[Agent Output]

    subgraph RAG_LAYER [RAG Retrieval Layer]
        R1[pgvector Cosine Search]
        R2[Cross-Encoder Re-rank]
        R1 --> R2
    end

    IN --> R1
    R2 --> HIL

    subgraph HIL_LAYER [Human-in-the-Loop - LangGraph Interrupt]
        HIL{Analyst Review}
        HIL -->|Approved| AUDIT[Audit Logger]
        HIL -->|Rejected| AUDIT
    end

    AUDIT --> DB

    subgraph DB [Data Layer - Aurora PostgreSQL + pgvector]
        D1[(ot_events)]
        D2[(asset_inventory)]
        D3[(cve_records)]
        D4[(threat_groups)]
        D5[(rag_chunks\nvector-1536)]
        D6[(anomaly_alerts)]
        D7[(approval_queue)]
        D8[(audit_log)]
    end

    subgraph INGEST [Ingestion Pipeline - Kafka + Python Workers]
        I1[Modbus / DNP3 / OPC-UA]
        I2[Syslog / PCAP / SCADA]
        I3[ICS-CERT / NVD Feeds]
        I4[MITRE ATT&CK ICS]
        I5[Worldview / ISAC]
    end

    I1 -->|Kafka| DB
    I2 -->|Kafka| DB
    I3 -->|Kafka| DB
    I4 -->|Kafka| DB
    I5 -->|Kafka| DB

    style RAG_LAYER fill:#e6fcf5,stroke:#20c997,stroke-width:2px
    style HIL_LAYER fill:#fff8e1,stroke:#f59f00,stroke-width:2px
    style DB        fill:#f0f4ff,stroke:#5c7cfa,stroke-width:2px
    style INGEST    fill:#fff0f6,stroke:#e64980,stroke-width:2px
    style HIL       fill:#ffe8cc,stroke:#e67700
    style AUDIT     fill:#f3f0ff,stroke:#7048e8
```

---

### Diagram 3 — AWS Deployment Architecture

```mermaid
flowchart LR
    subgraph USER [User Layer]
        U[Analyst - SOC]
    end

    subgraph FRONTEND [Frontend - EC2]
        SD[Streamlit Dashboard]
    end

    subgraph API [Agentic Core - ECS Fargate]
        FB[FastAPI + LangGraph]
    end

    subgraph AI [AI Layer - AWS Bedrock]
        LLM[TitanHaiku - LLM]
        EMB[Titan Embed - Embeddings]
    end

    subgraph STORAGE [Storage - AWS RDS]
        PG[(Aurora PostgreSQL\n+ pgvector)]
    end

    subgraph OBS [Observability]
        CW[CloudWatch Logs]
        S3[S3 - Exports]
    end

    U --> SD
    SD --> FB
    FB --> LLM
    FB --> EMB
    FB --> PG
    EMB --> PG
    FB --> CW
    FB --> S3

    style USER     fill:#f3f0ff,stroke:#7048e8,stroke-width:2px
    style FRONTEND fill:#e6fcf5,stroke:#20c997,stroke-width:2px
    style API      fill:#f0f4ff,stroke:#5c7cfa,stroke-width:2px
    style AI       fill:#fff8e1,stroke:#f59f00,stroke-width:2px
    style STORAGE  fill:#fff0f6,stroke:#e64980,stroke-width:2px
    style OBS      fill:#fafafa,stroke:#868e96,stroke-width:2px
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

Copyright (c) 2026. All rights reserved.

This repository and its contents are proprietary and confidential.
No part of this project may be copied, modified, distributed, or used
without explicit written permission from the author.

Shared for evaluation purposes only.
