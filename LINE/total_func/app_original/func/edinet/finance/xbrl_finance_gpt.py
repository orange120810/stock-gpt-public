import openai
import os
import json
from os import environ
from dotenv import load_dotenv
import sys
sys.path.append('../../../../')
from LINE.total_func.app_original.func.edinet.finance.xbrl_finance_prompt import setting_xbrl
from LINE.total_func.app_original.func.edinet.finance.xbrl_finance_data import pick_data_from_xbrl
load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

class annual_reports_analysis:

    def __init__(self,data):
        self.data = data

    def finance_gpt(self):
        try:
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                                {"role": "system", "content": setting_xbrl},
                                {"role": "user", "content": self.data},
                            ]
                        )
            advice_res = response['choices'][0]['message']['content']
            return advice_res
        except:
            None
