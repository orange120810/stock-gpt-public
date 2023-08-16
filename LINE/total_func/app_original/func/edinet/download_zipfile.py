import datetime
import requests
import pandas as pd
import time
import zipfile
from tqdm import tqdm

import sys
sys.path.append('../')

start_date = datetime.date(2023, 1,1)
end_date = datetime.date(2023, 8,5)

period = end_date - start_date
period = int(period.days)
day_list = []
for d in range(period):
    day = start_date + datetime.timedelta(days=d)
    day_list.append(day)
    
day_list.append(end_date)

#結果を格納するための空のリストを用意します
report_list =[]
#日付リストの期間に提出された書類のメタデータを取得してjson形式に変換します
for day in tqdm(day_list):
    url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"
    params = {"date": day, "type": 2}
    res = requests.get(url, params=params)
    json_data = res.json()
    #これを入れないとエラーになる。
    time.sleep(3)

    for num in range(len(json_data["results"])):
        ordinance_code= json_data["results"][num]["ordinanceCode"]
        form_code= json_data["results"][num]["formCode"]
        
	#ordinance_code=010かつform_code=030000が有価証券報告書になります
        if ordinance_code == "010" and  form_code =="030000" :
            company_name=json_data["results"][num]["filerName"]
            edi={ '会社名':company_name,
                        '書類名':json_data["results"][num]["docDescription"],           
                        'docID':json_data["results"][num]["docID"],
                        '証券コード':json_data["results"][num]["secCode"],
                        '日付': day             }
            report_list.append(edi)
        

df = pd.DataFrame(report_list)

docid_list = df["docID"].tolist()

filename_list = []

for docid in tqdm(docid_list):
    # 書類取得APIのエンドポイント
    url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents/" + docid
    print(url)
    
    # 書類取得APIのリクエストパラメータ
    params = {
        "type" : 1}
        
    # 出力ファイル名
    filename_list.append(docid + ".zip")

    # 書類取得APIの呼び出し
    res = requests.get(url, params=params, verify=False)
    # ファイルへ出力
    print(res.status_code)
    if res.status_code == 200:
        with open(docid +".zip", 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                f.write(chunk)