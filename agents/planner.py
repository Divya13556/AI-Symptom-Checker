# agents/planner.py
import asyncio
from llm_client import LLMClient
from typing import Dict, Any, List

class PlannerAgent:
    """
    Planner Agent: LLM-powered. Parses user input, identifies missing info,
    produces a plan (follow-up questions, which worker agents to call).
    """
    def __init__(self, llm: LLMClient):
        self.llm = llm

    async def plan(self, user_text: str, session: Dict[str, Any]) -> Dict[str,Any]:
        # Build a prompt (in production, use careful prompt templates)
        prompt = f"User describes: {user_text}\nExisting history: {session.get('history', [])}\nWhat follow-ups and candidate domains (respiratory,cardio,GI,neuro) should we query?"
        llm_out = await self.llm.generate(prompt)
        # STUB parsing: choose all workers when unsure
        plan = {
            "follow_ups": [
                "How long have you had these symptoms?",
                "Do you have fever, cough, chest pain, or shortness of breath?"
            ],
            "workers": ["respiratory","cardio","gi","neuro"],
            "note": llm_out
        }
        return plan
