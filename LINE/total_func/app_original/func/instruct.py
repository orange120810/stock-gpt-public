import os
from os import environ
import sys
sys.path.append('../../../')
from arelle import Cntlr
from LINE.total_func.app_original.choice_module_company import choice
from LINE.total_func.app_original.func.edinet.other_func.get_docID import getdocID
from LINE.total_func.app_original.func.scraping.technical.technical_data import technical_data
from LINE.total_func.app_original.func.scraping.technical.technical_gpt import technical_analysis
from LINE.total_func.app_original.func.edinet.finance.xbrl_finance_data import pick_data_from_xbrl
from LINE.total_func.app_original.func.edinet.finance.xbrl_finance_gpt import annual_reports_analysis
from LINE.total_func.app_original.func.edinet.htm.htm import pick_data_from_htm
from LINE.total_func.app_original.func.edinet.htm.htm_gpt import annual_reports_description
from LINE.total_func.app_original.func.chat.chat import chat_res
from LINE.total_func.app_original.func.scraping.fundamental.scraping_all_individual_info import scraping_all_info
from LINE.total_func.app_original.func.scraping.fundamental.fundamental_gpt import fundamental_analysis
from LINE.total_func.app_original.func.news.news import news_option
from LINE.total_func.db.sample_db import sample_db

class chat:
    def __init__(self,text):
        #モジュールと企業名、証券コードdocIDを取得する
        self.text = text
        self.choice_module = choice(self.text)
        self.company_name, self.security_code = self.choice_module.choice_company()
        self.module_gpt = self.choice_module.choice_module()
        self.getID = getdocID(self.company_name)
        self.docID = self.getID.get_docID()
        print(self.company_name,self.docID,self.module_gpt)

    def chat_module(self):
        try:
            if self.module_gpt == 'テクニカル分析':
                #テクニカル分析モジュール
                pandas_data = technical_data(self.security_code)
                sma_macd_rsi = pandas_data.SMA_macd_RSI().tail(5)
                tech_ana = technical_analysis(sma_macd_rsi)
                tech_ana.convert_df_to_dict()
                tech_ana.convert_dict_values_to_str()
                res = tech_ana.technical_res_gpt()
                return res
            
            elif self.module_gpt == "ファンダメンタル分析":
                db = sample_db()
                ana = db.fetch_company_ana(company_name=self.company_name)
                
                if ana != None:
                    return ana
                else:
                    #有価証券報告書モジュール
                    if self.docID != None:
                        #docIDに一致するディレクトリ以下からxbrlファイルの値を取得
                        prefix = "jpcrp030000"
                        suffix = ".xbrl"  
                        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'func','edinet','edinet_data','openfile',self.docID, 'XBRL', 'PublicDoc')
                        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'func','edinet','edinet_data','openfile')
                        files = os.listdir(dir_path)
                    
                        for filename in files:
                            if filename == self.docID:
                                target_dir = os.path.join(dir_path, self.docID, "XBRL", "PublicDoc")
                                target_files = os.listdir(target_dir)
                                for target_file in target_files:
                                    if target_file.startswith(prefix) and target_file.endswith(suffix):
                                        file_path = os.path.join(target_dir, target_file)
                                        break
                        
                        ctrl = Cntlr.Cntlr(logFileName="logToPrint")
                        model_xbrl = ctrl.modelManager.load(file_path)
                        facts = model_xbrl.facts 
                        #取得した財務データをGPT-4に分析してもらう
                        xbrl = pick_data_from_xbrl(facts=facts) 
                        all_finance_data = xbrl.select_all_info()
                        repo_ana = annual_reports_analysis(data=all_finance_data)
                        res = repo_ana.finance_gpt()
                        db = sample_db()
                        db.company_ana_to_db(company_name=self.company_name,company_ana=res)
                        return res
                    else:
                        None

            elif self.module_gpt == "企業情報":#データベースと連携
                    db = sample_db()
                    dis = db.fetch_company_dis(company_name=self.company_name)
                    #データベースに説明があったらそれを返す。無かったら新たに作ってデータベースへ入れる
                    if dis != None:
                        return dis
                    else:
                        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'func','edinet','edinet_data','openfile',self.docID, 'XBRL', 'PublicDoc')
                        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'func','edinet','edinet_data','openfile')
                        files = os.listdir(dir_path)
                    
                        for filename in files:
                            if filename == self.docID:
                                target_dir = os.path.join(dir_path, self.docID, "XBRL", "PublicDoc")
                                target_files = os.listdir(target_dir)
                                for target_file in target_files:
                                    if "0102010" in target_file:
                                        file_path = os.path.join(directory, target_file)
                                        break
                        
                        report = pick_data_from_htm(file_path=file_path)
                        repo_des = annual_reports_description(data=report)
                        res = repo_des.description_gpt()
                        db = sample_db()
                        db.company_dis_to_db(company_name=self.company_name,company_dis=res)
                        return res

            elif self.module_gpt == "ニュース":
                    news = news_option(user_message=self.text)
                    res = news.news_api_business()
                    # for i in range(len(res)):
                    #      print(res[i][0] + " : \n" + res[i][1])
                    return res

            elif self.module_gpt == "株式投資の情報":
                    chat = chat_res(data=self.text)
                    res = chat.stock_gpt()
                    return res

            elif self.module_gpt == "日常会話":
                    chat = chat_res(data=self.text)
                    res = chat.non_stock_gpt()
                    return res

            else:
                None
        except Exception as e:
             return e
         
