import json
import openai
import os
import json
from os import environ
from dotenv import load_dotenv
import sys
sys.path.append('../../../../')
from LINE.total_func.app_original.func.scraping.fundamental.fundamental_prompt import setting_fundamental

load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

#pandasのデータを受け取り、辞書型に変えたうえでChatGPTに送る
class fundamental_analysis:

    def __init__(self,repo_data,num_data):
        self.repo_data = repo_data
        self.num_data = num_data

    def fundamental_gpt(self):
        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": setting_fundamental},
                            {"role": "user", "content": f"{self.repo_data}/n{self.num_data}"},
                        ]
                    )
        res = response['choices'][0]['message']['content']
        return res






