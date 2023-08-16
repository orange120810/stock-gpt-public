import os
import json
from tqdm import tqdm
from arelle import Cntlr

class pick_data_from_xbrl:
    prefix = "jpcrp030000"
    suffix = ".xbrl"

    def __init__(self, docID):
        self.docID = docID
        self.directory = f"../edinet_data/openfile/{self.docID}/XBRL/PublicDoc/"
        for filename in os.listdir(self.directory):
            if filename.startswith(self.prefix) and filename.endswith(self.suffix):
                self.xbrl_file = os.path.join(self.directory, filename)

        ctrl = Cntlr.Cntlr(logFileName="logToPrint")
        model_xbrl = ctrl.modelManager.load(self.xbrl_file)
        self.facts = model_xbrl.facts

    def companyName(self):
        try:
            for fact in self.facts:
                if fact.concept.qname.localName == "FilerNameInJapaneseDEI":
                    return fact.value
        except Exception as e:
            print(e)

def get_company_names():
    # ディレクトリを走査して、docIDを取得する
    directory = "../edinet_data/openfile/"
    docIDs = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    # 各docIDに対して、企業名を取得する
    company_names = []
    for docID in tqdm(docIDs):
        data = pick_data_from_xbrl(docID)
        company_name = data.companyName()
        company_names.append({"docID": docID, "企業名": company_name})

    # 結果をJSON形式で保存する
    with open("company_names.json", "w") as f:
        json.dump(company_names, f, ensure_ascii=False, indent=4)

get_company_names()
