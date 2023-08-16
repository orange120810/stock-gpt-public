import json
import os

class getdocID:
    def __init__(self,company_name):
        self.company = company_name

    #有価証券報告書用のdocIDを検索  
    def get_docID(self):
        company_name = self.company
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'company_names.json')
        # JSONファイルを読み込む
        with open(file_path, "r") as f:
            data = json.load(f)

        # 入力された企業名に一致するdocIDを検索する
        for item in data:
            if company_name == item["企業名"]:
                return item["docID"]

        # 一致するdocIDが見つからなかった場合
        return None

