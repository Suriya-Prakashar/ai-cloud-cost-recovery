# AI Cloud Cost Forensics & Safe Recovery Agent

An agentic AI system built with LangGraph that detects AWS cost anomalies, investigates their root causes, evaluates optimization strategies, enforces safety policies, requests human approval, executes controlled remediation, verifies savings, and automatically rolls back unsafe changes.

## Current Status

Phase 1 — Project Foundation

### Phase 1 Components

* FastAPI backend
* Mock AWS service
* Simulated AWS billing data
* Simulated AWS resource data
* Health check API
* Swagger API documentation

### Architecture

```text
Client
   ↓
FastAPI
   ↓
Mock AWS Service
   ↓
Simulated AWS Data
```

### Planned Architecture

```text
AWS Account
    ↓
AWS STS
    ↓
AWS Services
    ↓
LangGraph
    ↓
Cost Analysis
    ↓
Forensics
    ↓
Optimization
    ↓
Risk & Policy
    ↓
Human Approval
    ↓
Controlled Execution
    ↓
Verification
    ↓
Rollback if Required
```

## Technology Stack

* Python
* FastAPI
* LangGraph
* LangChain
* AWS
* boto3
* MongoDB
* React
* Docker

## Development Strategy

The project is being developed incrementally.

Each phase follows:

```text
Implement
   ↓
Run
   ↓
Test
   ↓
Fix
   ↓
Git Commit
   ↓
GitHub Push
   ↓
Next Phase
```
