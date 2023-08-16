from os import environ
from typing import Dict

from dotenv import load_dotenv
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, Source, TextMessage, TextSendMessage


from LINE.total_func.app_original.instruct import chat
from LINE.total_func.db.sample_db import sample_db

load_dotenv(".env", verbose=True)

app = Flask(__name__)

if not (access_token := environ.get("LINE_CHANNEL_ACCESS_TOKEN")):
    raise Exception("access token is not set as an environment variable")

if not (channel_secret := environ.get("LINE_CHANNEL_SECRET")):
    raise Exception("channel secret is not set as an environment variable")

line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(channel_secret)

#{[userid = 000000, ChatGPTClient = gpt-client],
# [userid = 000001, ChatGPTClient = gpt-client]}
#ユーザーごとのgpt-clientを辞書形式でchatgpt_instance_mapに保存
# chatgpt_instance_map: Dict[str, ChatGPTClient] = {}

@app.route("/")
def hello():
    return "Hello World"

#LINEからのpostリクエストの検証
@app.route("/callback", methods=["POST"])
def callback() -> str:
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

#メッセージイベントが発生したときに実行される機能
@handler.add(MessageEvent, message=TextMessage)

def handle_message(event: MessageEvent) -> None:
    
    #テキスト・トーク元・ユーザーidを取得
    text_message: TextMessage = event.message
    source: Source = event.source
    user_id: str = source.user_id
    
    if text_message.text == '使い方':
        return None
    else:#データベースと連携
        db = sample_db()
        num = db.sample(user_id=user_id)
        if num >= 100:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='今日の会話上限に達しました'))
        else:    
            print(text_message.text)
            gpt_chat = chat(text=text_message.text)
            res = str(gpt_chat.chat_module())
            print(res)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=res))
            
            db.text_to_db(user_id = user_id,user_text=text_message.text,ai_text=res)
        
        
    
     

   