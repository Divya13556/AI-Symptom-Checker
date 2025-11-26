# agents/evaluator.py
from typing import List, Dict, Any
from tools import fever_severity

class EvaluatorAgent:
    """
    Verifies worker outputs and enforces safety rules.
    Produces final triage recommendation: 'self-care', 'see primary care', 'urgent care'
    """
    def __init__(self):
        pass

    def evaluate(self, worker_results: List[Dict[str,Any]], facts: Dict[str,Any]) -> Dict[str,Any]:
        # find highest scoring domain
        top = max(worker_results, key=lambda r: r["score"])
        # red flag detection
        red_flags = []
        if facts.get("chest_pain") and facts.get("shortness_of_breath"):
            red_flags.append("possible cardiac emergency")
        if facts.get("fever_temp_c") and facts["fever_temp_c"] >= 40.0:
            red_flags.append("very high fever")

        if red_flags:
            recommendation = "urgent_care"
            reason = f"Red flags: {red_flags}"
        elif top["score"] >= 0.8:
            recommendation = "see_primary_care"
            reason = f"Likely: {top['domain']}. Confidence: {top['score']}"
        else:
            recommendation = "self_care"
            reason = f"Low confidence across domains. Top: {top['domain']} ({top['score']})"

        return {
            "top_domain": top["domain"],
            "top_score": top["score"],
            "recommendation": recommendation,
            "reason": reason,
            "worker_results": worker_results
        }
