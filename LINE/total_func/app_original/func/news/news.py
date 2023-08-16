import openai
import os
import json
from os import environ
from dotenv import load_dotenv
import sys
import pprint
import requests
import pandas as pd

from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import load_tools
from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

sys.path.append('../../../../')
load_dotenv()
openai.api_key = os.getenv('CHATGPT_API_KEY')

google_api_key = environ.get("SERP_API_KEY")
serper_api_key = environ.get("SERPER_API_KEY")
news_api_key = environ.get("NEWS_API_KEY")
key = environ.get("CHATGPT_API_KEY")
openai.api_key = key

class news_option:
    def __init__(self,user_message) :
        self.llm = OpenAI(temperature=0, openai_api_key = key)
        self.chat = ChatOpenAI(temperature=0, openai_api_key = key)
        self.user_message = user_message
        self.prompt = PromptTemplate.from_template("あなたは優秀なアシスタントです。以下のユーザーの質問に対して正確で分かりやすい返答を返します。:{user}")
        prompt_value = self.prompt.format_prompt(user=self.user_message)
        self.text = prompt_value.to_string()
        
    #google検索、精度が良くない
    def serpapi(self):
        tools = load_tools(["serpapi", "llm-math"], llm=self.llm, serpapi_api_key = google_api_key)
        agent = initialize_agent(tools, self.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
        res = agent.run(self.text)
        return res
    
    #serper精度はそれなりだが英語での返答
    def serper(self):
        search = GoogleSerperAPIWrapper()
        tools = [
            Tool(
                name="Intermediate Answer",
                func=search.run,
                description="useful for when you need to ask with search"
            )
        ]

        self_ask_with_search = initialize_agent(tools, self.llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
        res = self_ask_with_search.run(self.text)
        return res
    
    #和訳するメソッド
    def english_to_japanese(self,text):
        try:
            response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                                {"role": "system", "content": "ユーザーから送られてくる英文を日本語に訳しなさい。訳せばいいだけで追加で情報を加える必要はない。"},
                                {"role": "user", "content": text},
                            ]
                        )
            res = response['choices'][0]['message']['content']
            return res
        except:
            None
    
    #ニュースのタイトル、要約を取得できる
    def news_api_all(self):
        try:
            pd.options.display.max_colwidth = 25
            headers = {'X-Api-Key': news_api_key}
            url = 'https://newsapi.org/v2/everything'
            params = {
                'q': self.user_message,
                'sortBy': 'publishedAt',
                'pageSize': 10
            }

            response = requests.get(url, headers=headers, params=params)

            if response.ok:
                data = response.json()
                df = pd.DataFrame(data['articles'])
                modified_df = df[['title', 'description','url']]
                title = str(modified_df['title'][0])
                description = str(modified_df['description'][0]),
                source_url = modified_df["url"][0]
                res = [title,description,source_url]
                return res
            
        except Exception as e:
            return e
    
    #最新のニュース5件取得
    def news_api_business(self):
        try:
            # Top headlines Endpoint
            headers = {'X-Api-Key': news_api_key}
            url = 'https://newsapi.org/v2/top-headlines'
            params = {
                'category': 'business',
                'country': 'jp',
                'pageSize': 5
            }

            # Get response
            response = requests.get(url, headers=headers, params=params)

            # Make dataframe
            if response.ok:
                data = response.json()
                df = pd.DataFrame(data['articles'])
                modified_df = df[['title', 'url']]

                res = []

                for i in range(len(modified_df.index)):
                    title = str(modified_df['title'][i])
                    source_url = str(modified_df["url"][i])
                    res.append([title,source_url])

            return res
                
        except Exception as e:
            return e




