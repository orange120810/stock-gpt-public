import openai
import os
import json
from os import environ
from dotenv import load_dotenv
import sys
sys.path.append('../../../../')
from LINE.total_func.app_original.func.edinet.htm.htm_prompt import setting_htm
from LINE.total_func.app_original.func.edinet.finance.xbrl_finance_data import pick_data_from_xbrl
load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

class annual_reports_description:

    def __init__(self,data):
        self.data = data
        n = 10000
        self.parts = [self.data[i:i+n] for i in range(0, len(self.data), n)]
        self.text = self.parts[:2]
        print(len(self.parts))
    
    def summarize(self,div_text):
        response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-16k",#"gpt-3.5-turbo-16k"
                        messages=[
                                {"role": "system", "content": setting_htm},
                                {"role": "user", "content": f"何を行っている企業か分かるよう事業内容を中心に抽出して1000字程度に要約しなさい。具体的なサービス名があればそれを含めること。改行はいらない。: {div_text}"},
                            ]
                        )
        res = response['choices'][0]['message']['content']
        return res

    def final_summarize(self,dis_text):
        response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                                {"role": "system", "content": setting_htm},
                                {"role": "user", "content": f"何を行っている企業か分かるよう事業内容を中心に抽出して300字程度に要約しなさい。具体的なサービス名があればそれを含めること。出だしはこの企業はで始めなさい。見やすいように改行など工夫をしてください: {dis_text}"},
                            ]
                        )
        res = response['choices'][0]['message']['content']
        return res

    def description_gpt(self):
        try:
            summaries = [self.summarize(div_text=part) for part in self.text]
            final_summary = self.final_summarize(dis_text=' '.join(summaries))
            return final_summary
        except Exception as e:
            return e
