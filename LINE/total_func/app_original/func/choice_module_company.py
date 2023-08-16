import openai
from openai.embeddings_utils import cosine_similarity
import os
from os import environ
from LINE.total_func.app_original.module_setting import setting_prompt
import sys
sys.path.append('../../../')
import json
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

class choice:

    def __init__(self, text):
        self.text = text
    #GPTによるモジュール選択
    def choice_module(self):
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": setting_prompt},
                    {"role": "user", "content": self.text},
                ]
            )

        module_res = response['choices'][0]['message']['content']
        return module_res
    
    #企業名を検索
    def choice_company(self):

        file_path_em = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'companyName_securityCode_embeddings.json')
        
        # データベースの読み込み
        with open(file_path_em) as f:
            INDEX = json.load(f)

        # ユーザーのテキストをベクトル化
        query = openai.Embedding.create(
            model='text-embedding-ada-002',
            input=self.text
        )

        query = query['data'][0]['embedding']

        # 総当りで類似度を計算
        results = map(
                lambda i: {
                    'company_name': i['company_name'],
                    'security_code': i['security_code'],
                    # ここでクエリと各文章のコサイン類似度を計算
                    'similarity': cosine_similarity(i['embedding'], query)
                    },
                INDEX
        )
        # コサイン類似度で降順（大きい順）にソート
        results = sorted(results, key=lambda i: i['similarity'], reverse=True)

        # 類似度の高いモジュールをの名前を取得
        self.best_company_name: str = results[0]["company_name"]
        self.best_company_security_code = int(results[0]["security_code"])

        return self.best_company_name ,self.best_company_security_code


