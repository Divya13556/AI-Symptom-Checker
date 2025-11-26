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

## How It Works

When a user submits their symptoms, the Planner Agent generates relevant follow-up questions. Multiple Worker Agents (for respiratory, cardiac, GI, neuro domains) score symptom severity in parallel. The Evaluator Agent reviews risk scores and red-flags to safely recommend next steps, such as home care, seeing a doctor, or urgent intervention. All tasks are logged for review.

### Example API Interactions

(screenshots/Screenshot-17.jpg)  
_User input case with fever and persistent cough. Shows how the agent analyzes respiratory symptoms and asks for relevant follow-up questions._

(screenshots/Screenshot-18.jpg)  
_Agent response for a mild case: “self_care” recommendation with low confidence across domains, demonstrating conservative triage for non-serious symptoms._

(screenshots/Screenshot-19.jpg)  
_Response body detailing parallel worker agent scores, confirming multi-domain medical reasoning and transparency in evaluation._

(screenshots/Screenshot-21.jpg)  
_Another user request example. Highlights clear input format and agent’s ability to parse varied symptom presentations._

(screenshots/Screenshot-22.jpg)  
_Shows decision logic where “self_care” is advised—demonstrates project’s safe medical advice for benign headache and nausea symptoms._

(screenshots/Screenshot-23.jpg)  
_Final JSON response example for GI-related symptoms, documenting how your agent combines scores and notes from all worker agents for output._

(screenshots/Screenshot-24.jpg)  
_Agent recommending “urgent_care” due to detected red flags in chest pain and shortness of breath, displaying strict medical safety protocol._


## Limitations & Disclaimer

This agent provides only conservative triage recommendations—it does **not** diagnose conditions, and is **not a substitute for professional medical advice, diagnosis, or treatment**. Always consult a qualified physician for any serious symptoms.


