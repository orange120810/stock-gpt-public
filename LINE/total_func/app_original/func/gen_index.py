import openai
import os
from os import environ
import json

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

# 入力用の文章をロード
with open('companyName_securityCode.json') as f:
    docs = json.load(f)

index = []
for i, doc in enumerate(docs):
    # ここでベクトル化を行う
    res = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=doc["company_name"]
    )

    # ベクトルをデータベースに追加
    index.append({
        "company_name": doc["company_name"],
        "security_code": doc["security_code"],
        "embedding": res["data"][0]["embedding"]
    })

    print(f'Processed {i+1} of {len(docs)} documents')


with open(f'companyName_securityCode_embeddings.json', 'w') as f:
    json.dump(index, f)

