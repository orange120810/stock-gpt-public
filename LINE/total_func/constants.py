from enum import Enum

#OpenAIのrole
class Role(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

#OpenAIのmodel
class Model(Enum):
    GPT4 = "gpt-4"