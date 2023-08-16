from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from constants import Role

#会話履歴を辞書や値に変換するクラス
@dataclass
class Message:
    role: Role
    content: str

    #会話を辞書型に変換する
    def to_dict(self) -> Dict[str, str]:
        return {"role": self.role.value, "content": self.content}
    
    #会話を値に変換する
    @classmethod
    def from_dict(cls, message: Dict[str, str]) -> Message:
        return cls(role=Role(message["role"]), content=message["content"])