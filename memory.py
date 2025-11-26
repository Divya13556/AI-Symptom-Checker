import json
from typing import Dict, Any
from pathlib import Path

class InMemorySessionService:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def get(self, session_id: str) -> Dict[str, Any]:
        return self.sessions.setdefault(session_id, {"history": []})

    def append_history(self, session_id: str, entry: Dict[str, Any]):
        sess = self.get(session_id)
        sess["history"].append(entry)

class MemoryBank:
    def __init__(self, path="memory_bank.json"):
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text(json.dumps({}))

    def save_user(self, user_id: str, data: Dict[str, Any]):
        d = json.loads(self.path.read_text())
        d[user_id] = data
        self.path.write_text(json.dumps(d, indent=2))

    def load_user(self, user_id: str):
        d = json.loads(self.path.read_text())
        return d.get(user_id)
