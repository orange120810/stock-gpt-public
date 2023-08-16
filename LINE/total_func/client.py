from dataclasses import dataclass, field
from os import environ
from typing import List

import openai
from openai.openai_object import OpenAIObject

from constants import Model
from message import Message
from settings import system_settings_1

@dataclass #dataclassは__init__などを自動生成
class ChatGPTClient:
    model: Model
    messages: List[Message] = field(default_factory=list)
    
    #openAIのAPIkeyの確認
    def __post_init__(self) -> None:
        if not (key := environ.get("CHATGPT_API_KEY")):
            raise Exception(
                "ChatGPT api key is not set as an environment variable"
            )
        openai.api_key = key

    #Messageクラスをmessagesリストに格納
    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    #OpenAIにテキストを渡し返答を得る
    def create(self) -> OpenAIObject:
        res = openai.ChatCompletion.create(
            model=self.model.value,
            messages=[{"role": "system", "content": system_settings_1}] + [m.to_dict() for m in self.messages],
        )
        self.add_message(Message.from_dict(res["choices"][0]["message"]))
        return res