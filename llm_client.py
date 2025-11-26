from typing import Dict

class LLMClient:
    def __init__(self, provider="stub"):
        self.provider = provider

    async def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Replace this function with an actual call to OpenAI, Anthropic, or Gemini.
        For tests, this returns a deterministic stubbed response.
        """
       
        return f"[LLM STUB RESPONSE] Summary of prompt: {prompt[:200]}"
