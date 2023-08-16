import json
import openai
import os
import json
from os import environ
from dotenv import load_dotenv
import sys
sys.path.append('../../../../')
from LINE.total_func.app_original.func.scraping.technical.technical_prompt import setting_technical

load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

#pandasのデータを受け取り、辞書型に変えたうえでChatGPTに送る
class technical_analysis:

    def __init__(self,data):
        self.data = data

    def convert_df_to_dict(self):
        self.df_dict = self.data.to_dict(orient='list')
        return self.df_dict

    def convert_dict_values_to_str(self):
        self.new_dict = {}
        for key, value in self.df_dict.items():
            if isinstance(value, list):
                self.new_dict[key] = [str(item) for item in value]
            else:
                self.new_dict[key] = str(value)
        return self.new_dict

    def technical_res_gpt(self):
        response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                            {"role": "system", "content": setting_technical},
                            {"role": "user", "content": json.dumps(self.new_dict)},
                        ]
                    )
        advice_res = response['choices'][0]['message']['content']
        return advice_res
    
    def choice_module(self, num):
        if num == '1':   
            self.convert_df_to_dict()
            self.convert_dict_values_to_str()
            res = self.res_gpt()
            print(res)

        elif num == '2':
            self.convert_df_to_dict()
            self.convert_dict_values_to_str()
            res = self.res_gpt()
            print(res)

        elif num == '3':
            self.convert_df_to_dict()
            self.convert_dict_values_to_str()
            res = self.res_gpt()
            print(res)

        elif num == '4':
            self.convert_df_to_dict()
            self.convert_dict_values_to_str()
            res = self.res_gpt()
            print(res)

        else:
            print('適切な数字以外が入力されました')






