# agents/worker.py
import asyncio
from typing import Dict, Any
from tools import compute_bmi, fever_severity

class WorkerAgent:
    """
    Generic worker agent that evaluates a hypothesis bucket.
    Each worker runs concurrently to score plausibility and produce suggestions.
    """
    def __init__(self, name: str):
        self.name = name

    async def evaluate(self, facts: Dict[str,Any]) -> Dict[str,Any]:
        # Simulate compute time
        await asyncio.sleep(0.5)
        # Simple heuristics
        score = 0.1
        notes = []
        if self.name == "respiratory":
            if facts.get("cough"): score += 0.6; notes.append("cough present")
            if facts.get("fever") and facts.get("shortness_of_breath"): score += 0.2
        if self.name == "cardio":
            if facts.get("chest_pain"): score += 0.7; notes.append("chest pain")
        if self.name == "gi":
            if facts.get("nausea") or facts.get("vomiting"): score += 0.6
        if self.name == "neuro":
            if facts.get("headache") and facts.get("confusion"): score += 0.6
        return {"domain": self.name, "score": round(score,2), "notes": notes}
