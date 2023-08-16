import openai
import os
import json
from os import environ
from dotenv import load_dotenv
import sys
sys.path.append('../../../../')
load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

class chat_res:

    def __init__(self,data):
        self.data = data

    def stock_gpt(self):
        try:
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                                {"role": "system", "content": "投資のプロとしてふるまいなさい"},
                                {"role": "user", "content": self.data},
                            ]
                        )
            advice_res = response['choices'][0]['message']['content']
            return advice_res
        except:
            None
    
    def non_stock_gpt(self):
        try:
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                                {"role": "system", "content": "ユーザーからの日常会話に優しく対応しなさい。絶対に非倫理的、エロ、グロには私は分かりませんと返答しなさい"},
                                {"role": "user", "content": self.data},
                            ]
                        )
            advice_res = response['choices'][0]['message']['content']
            return advice_res
        except:
            None
    
    

