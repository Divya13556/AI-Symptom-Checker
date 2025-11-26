import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.planner import PlannerAgent
from agents.worker import WorkerAgent
from agents.evaluator import EvaluatorAgent
from llm_client import LLMClient
from memory import InMemorySessionService, MemoryBank
import asyncio

app = FastAPI(title="AI Symptom Checker Agent")

llm = LLMClient()
planner = PlannerAgent(llm)
evalu = EvaluatorAgent()

session_svc = InMemorySessionService()
mem_bank = MemoryBank()

class SymptomRequest(BaseModel):
    session_id: str
    user_text: str
    facts: dict = {}

@app.post("/symptom_check")
async def symptom_check(req: SymptomRequest):
    session = session_svc.get(req.session_id)
    plan = await planner.plan(req.user_text, session)
    session_svc.append_history(req.session_id, {"user": req.user_text})
    worker_names = plan["workers"]
    workers = [WorkerAgent(name) for name in worker_names]
    coros = [w.evaluate(req.facts) for w in workers]
    worker_results = await asyncio.gather(*coros)
    final = evalu.evaluate(worker_results, req.facts)
    session_svc.append_history(req.session_id, {"assistant": final})
    return {"plan": plan, "worker_results": worker_results, "final": final}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
