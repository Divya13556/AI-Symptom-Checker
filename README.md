# AI Symptom Checker Agent

## Overview
A multi-agent conversational triage assistant that asks guided clinical questions, runs parallel hypothesis analyses, and provides conservative next-step recommendations.

## Features
- Planner Agent (LLM-powered) for follow-up question planning
- Parallel Symptom Analysis Agents (respiratory, cardiovascular, GI, neuro)
- Medical Safety Evaluator Agent with red-flag detection
- Custom tools (Vitals processing), session state and optional long-term memory
- Observability: structured logs and simple metrics
- Pause/resume support for long-running tasks

## Quickstart (local)
1. Clone repo
2. Create virtual env:

python -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
3. Run:

uvicorn main:app --reload
4. Open `http://localhost:8000/docs` for the API UI.

## Files
- `main.py` - FastAPI endpoint and orchestration
- `agents/` - Planner, Worker, Evaluator implementations
- `tools.py` - VitalsTool and helpers
- `memory.py` - Session and long-term memory
- `llm_client.py` - LLM interface (stub - configure with provider)
- `requirements.txt` - Python deps

## Deployment
- Cloud Run / Agent Engine recommended. See DEPLOYMENT.md for steps.

## Safety
- Not a medical device. Provide clear disclaimer.
- Conservative recommendations by default.
