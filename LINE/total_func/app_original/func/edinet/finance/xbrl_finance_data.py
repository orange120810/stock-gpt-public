import os
from arelle import Cntlr
import sys
sys.path.append("../../../")
sys.path.append("app_original/func/edinet/edinet_data/openfile/")
# 売上高
net_sales = "NetSalesSummaryOfBusinessResults"
# 経常利益又は経常損失
ordinary_income_loss = "OrdinaryIncomeLossSummaryOfBusinessResults"
#当期純利益又は当期純損失
net_income_loss = "NetIncomeLossSummaryOfBusinessResults"
# 親会社に帰属する当期純利益又は親会社に帰属する当期純損失
profit_loss = "ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults"
# 包括利益
comprehensive_income = "ComprehensiveIncomeSummaryOfBusinessResults"
# 純資産額
net_assets = "NetAssetsSummaryOfBusinessResults"
# 総資産額
total_assets = "TotalAssetsSummaryOfBusinessResults"
# １株当たり純資産額     
net_assets_pershare = "NetAssetsPerShareSummaryOfBusinessResults"
# １株当たり当期純利益又は当期純損失
basic_earnings_loss_pershare = "BasicEarningsLossPerShareSummaryOfBusinessResults"
# 潜在株式調整後１株当たり当期純利益
diluted_earnings_pershare = "DilutedEarningsPerShareSummaryOfBusinessResults"
# 自己資本比率
equity_to_asset_ratio = "EquityToAssetRatioSummaryOfBusinessResults"
# 自己資本利益率
rate_of_return_on_equity = "RateOfReturnOnEquitySummaryOfBusinessResults"
# 株価収益率
price_earnigs_ratio = "PriceEarningsRatioSummaryOfBusinessResults"
# 持分法を適用した場合の投資利益
equity_earning_loss_equity_meathod = "EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults"
#資本金
capital_stock = "CapitalStockSummaryOfBusinessResults"
#発行済み株式総数
total_issued_share = "TotalNumberOfIssuedSharesSummaryOfBusinessResults"
#1株あたり純資産額
net_asset_pershare = "NetAssetsPerShareSummaryOfBusinessResults"
#1株あたり配当額
dividend_paid_per_share = "DividendPaidPerShareSummaryOfBusinessResults"
#1株あたり中間配当額
interim_dividend_paid_per_share = "InterimDividendPaidPerShareSummaryOfBusinessResults"
#配当性向
payout_ratio = "PayoutRatioSummaryOfBusinessResults"
# 営業活動によるキャッシュ・フロー
net_cach_provided_by_used_in_operatind_activities = (
    "NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults"
)
# 投資活動によるキャッシュ・フロー
net_cach_provided_by_used_in_investing_activities = (
    "NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults"
)
# 財務活動によるキャッシュ・フロー
net_cach_provided_by_used_in_financing_activities = (
    "NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults"
)
# 現金及び現金同等物の期末残高
cash_and_cash_equivalents = "CashAndCashEquivalentsSummaryOfBusinessResults"
# 従業員数
number_of_employees = "NumberOfEmployees"
#従業員平均年齢
average_age_employees = "AverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees"
#平均勤続年数
average_length_of_service = "AverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees"
#平均給与額
average_annual_salary = "AverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees"

# 平均臨時雇用者数
average_number_of_temporary_workers = "AverageNumberOfTemporaryWorkers"
# 株主総利回り
total_sahre_holder_return = "TotalShareholderReturn"

# 連結決算期間５年間(Duration)
prior_4_duration = "Prior4YearDuration"
prior_3_duration = "Prior3YearDuration"
prior_2_duration = "Prior2YearDuration"
prior_1_duration = "Prior1YearDuration"
prior_0_duration = "CurrentYearDuration"

# 連結決算期間５年間(Instant)
prior_4_instant = "Prior4YearInstant"
prior_3_instant = "Prior3YearInstant"
prior_2_instant = "Prior2YearInstant"
prior_1_instant = "Prior1YearInstant"
prior_0_instant = "CurrentYearInstant"


# 単体決算期間５年
prior_4_alone = "Prior4YearDuration_NonConsolidatedMember"
prior_3_alone = "Prior3YearDuration_NonConsolidatedMember"
prior_2_alone = "Prior2YearDuration_NonConsolidatedMember"
prior_1_alone = "Prior1YearDuration_NonConsolidatedMember"
prior_0_alone = "CurrentYearDuration_NonConsolidatedMember"

#単体連結決算５年
prior_4_alone_instant = "Prior4YearInstant_NonConsolidatedMember"
prior_3_alone_instant = "Prior3YearInstant_NonConsolidatedMember"
prior_2_alone_instant = "Prior2YearInstant_NonConsolidatedMember"
prior_1_alone_instant = "Prior1YearInstant_NonConsolidatedMember"
prior_0_alone_instant = "CurrentYearInstant_NonConsolidatedMember"

# 決算年度
prior_4_year = 2018
prior_3_year = 2019
prior_2_year = 2020
prior_1_year = 2021
prior_0_year = 2022

# xbrlファイルからデータをとる処理をまとめたクラス
class pick_data_from_xbrl: 

    def __init__(self,facts):
        self.facts = facts
        self.results = ""
        # self.docID = docID
        # prefix = "jpcrp030000"
        # suffix = ".xbrl"  
        # self.directory = f"../edinet_data/openfile/{self.docID}/XBRL/PublicDoc/"
        # self.dir_path = "app_original/func/edinet/edinet_data/openfile/"
        # files = os.listdir(self.dir_path)
        # for filename in files:
        #     if filename == self.docID:
        #         target_dir = os.path.join(self.dir_path, self.docID, "XBRL", "PublicDoc")
        #         target_files = os.listdir(target_dir)
        #         for target_file in target_files:
        #             if target_file.startswith(prefix) and target_file.endswith(suffix):
        #                 self.file_path = os.path.join(target_dir, target_file)
        #                 break

                

        # ctrl = Cntlr.Cntlr(logFileName="logToPrint")
        # model_xbrl = ctrl.modelManager.load(self.file_path)
        # self.facts = model_xbrl.facts 

    #連結決算のタグが存在しているか確認
    def search_existence_connect(self,tag):
        tag_existence = False
        for fact in self.facts:
            if fact.concept.qname.localName == tag and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                tag_existence = True
                return tag_existence
        return None
    
    #単体決算が存在しているか確認
    def search_existence_alone(self,tag):
        tag_existence = False
        for fact in self.facts:
            if fact.concept.qname.localName == tag and (fact.contextID == prior_0_alone_instant or fact.contextID == prior_0_alone):
                tag_existence = True
                return tag_existence
        return None
    
     #値の型判定（使用しない）
    def search_type(self, tag):
        value_type = None
        for fact in self.facts:
            if fact.concept.qname.localName == tag:
                value = fact.value
                value_type = type(value)
                return value_type
        return None
    
    # 会社の名前
    def companyName(self):
        try:
            for fact in self.facts:
                if fact.concept.qname.localName == "FilerNameInJapaneseDEI":
                    self.results += f"企業名：{fact.value}\n"
        except:
            return None
        return self.results

    # 連結売上高
    def netSales(self):
        try:
            tag_existence = self.search_existence_connect(net_sales)
            if tag_existence == True:
                self.results += "連結決算　売上高（円）\n"
                for fact in reversed(self.facts):                    
                    if   fact.concept.qname.localName == net_sales and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

    # 連結経常利益又は経常損失
    def ordinaryIncomeLoss(self):
        try:
            tag_existence = self.search_existence_connect(ordinary_income_loss)
            if tag_existence == True:
                self.results += "連結決算　経常利益又は経常損失（円）\n"
                for fact in reversed(self.facts): 
                    if   fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 親会社に帰属する当期純利益又は親会社に帰属する当期純損失
    def profitLoss(self):
        try:
            tag_existence = self.search_existence_connect(profit_loss)
            if tag_existence == True:  
                self.results += "連結決算　親会社に帰属する当期純利益又は親会社に帰属する当期純損失（円）\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == profit_loss and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 包括利益
    def comprehensiveIncome(self):
        try:
            tag_existence = self.search_existence_connect(comprehensive_income)
            if tag_existence == True:  
                self.results += "連結決算　包括利益（円）\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
        
     # 純資産額
    def netAssets(self):
        try:
            tag_existence = self.search_existence_connect(net_assets)
            if tag_existence == True:  
                self.results += "連結決算　純資産額（円）\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_assets and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
     
    # 総資産額
    def totalAssets(self):
        try:
            tag_existence = self.search_existence_connect(total_assets)
            if tag_existence == True:  
                self.results += "連結決算　総資産額（円）\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == total_assets and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # １株当たりの純資産額
    def netAssetsPershare(self):
        try:
            tag_existence = self.search_existence_connect(net_assets_pershare)
            if tag_existence == True: 
                self.results += "連結決算　１株当たりの純資産額（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + float(fact.value) + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # １株当たり当期純利益又は当期純損失
    def basicEarningsLossPershare(self):
        try:
            tag_existence = self.search_existence_connect(basic_earnings_loss_pershare)
            if tag_existence == True: 
                self.results += "連結決算　１株当たり当期純利益又は当期純損失（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + float(fact.value) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + float(fact.value) + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
     # 潜在株式調整後１株当たり当期純利益
    def dilutedEarningsPershare(self):
        try:
            tag_existence = self.search_existence_connect(diluted_earnings_pershare)
            if tag_existence == True: 
                self.results += "連結決算　潜在株式調整後１株当たり当期純利益（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_0_instant or fact.contextID == prior_0_duration):
                        self.results += f"{prior_0_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_1_instant or fact.contextID == prior_1_duration):
                        self.results += f"{prior_1_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_2_instant or fact.contextID == prior_2_duration):
                        self.results += f"{prior_2_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_3_instant or fact.contextID == prior_3_duration):
                        self.results += f"{prior_3_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_4_instant or fact.contextID == prior_4_duration):
                        self.results += f"{prior_4_year} :" + format(float(fact.value)) + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
                
    #以下単体決算取得メソッド
    # 単体売上高
    def netSales_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_sales)
            if tag_existence == True:
                self.results += "単独決算　売上高（円）" + "\n"
                for fact in reversed(self.facts):            
                    if fact.concept.qname.localName == net_sales and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_sales and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

    # 単体の経常利益又は経常損失
    def ordinaryIncomeLoss_alone(self):
        try:
            tag_existence = self.search_existence_alone(ordinary_income_loss)
            if tag_existence == True:
                self.results += "単独決算　経常利益又は経常損失（円）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == ordinary_income_loss and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の親会社に帰属する当期純利益又は親会社に帰属する当期純損失
    def profitLoss_alone(self):
        try:
            tag_existence = self.search_existence_alone(profit_loss)
            if tag_existence == True:
                self.results += "単独決算　親会社に帰属する当期純利益又は親会社に帰属する当期純損失（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == profit_loss and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == profit_loss and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

    # 単体の当期純利益又は当期純損失
    def netIncomeLoss_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_income_loss)
            if tag_existence == True:
                self.results += "単独決算　当期純利益又は当期純損失（円）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == net_income_loss and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_income_loss and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_income_loss and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_income_loss and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_income_loss and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 持分法を適用した場合の投資利益
    def equityEarningLossEquityAlone(self):
        try:
            tag_existence = self.search_existence_alone(equity_earning_loss_equity_meathod)
            if tag_existence == True:
                self.results += "単独決算　持分法を適用した場合の投資利益" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == equity_earning_loss_equity_meathod and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_earning_loss_equity_meathod and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_earning_loss_equity_meathod and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_earning_loss_equity_meathod and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_earning_loss_equity_meathod and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None     
        except:
            return None
        return self.results
    
    # 単体の資本金
    def capitalStock_alone(self):
        try:
            tag_existence = self.search_existence_alone(capital_stock)
            if tag_existence == True:
                self.results += "単独決算　資本金（円）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == capital_stock and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == capital_stock and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == capital_stock and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == capital_stock and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == capital_stock and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

    
    # 単体の包括利益
    def comprehensiveIncome_alone(self):
        try:
            tag_existence = self.search_existence_alone(comprehensive_income)
            if tag_existence == True:
                self.results += "単独決算　包括利益（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == comprehensive_income and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None  
        except:
            return None
        return self.results
    
    # 単体の発行済株式総数
    def totalIssuedShare_alone(self):
        try:
            tag_existence = self.search_existence_alone(total_issued_share)
            if tag_existence == True:
                self.results += "単独決算　発行済株式総数（株）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == total_issued_share and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_issued_share and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_issued_share and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_issued_share and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_issued_share and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
        
     # 単体の純資産額
    def netAssets_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_assets)
            if tag_existence == True:
                self.results += "単独決算　純資産額（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_assets and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_assets and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None 
        except:
            return None
        return self.results
     
    # 単体の総資産額
    def totalAssets_alone(self):
        try:
            tag_existence = self.search_existence_alone(total_assets)
            if tag_existence == True:
                self.results += "単独決算　総資産額（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == total_assets and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_assets and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の１株当たりの純資産額
    def netAssetsPershare_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_assets_pershare)
            if tag_existence == True:
                self.results += "単独決算　１株当たりの純資産額（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == net_assets_pershare and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value)) + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の1株当たり配当額
    def dividendPaidShare_alone(self):
        try:
            tag_existence = self.search_existence_alone(dividend_paid_per_share)
            if tag_existence == True:
                self.results += "単独決算　１株当たり配当額（円）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == dividend_paid_per_share and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == dividend_paid_per_share and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == dividend_paid_per_share and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == dividend_paid_per_share and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == dividend_paid_per_share and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の１株当たり中間配当額
    def interDividendPaidShare_alone(self):
        try:
            tag_existence = self.search_existence_alone(interim_dividend_paid_per_share)
            if tag_existence == True:
                self.results += "単独決算　１株当たり中間配当額（円）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == interim_dividend_paid_per_share and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == interim_dividend_paid_per_share and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == interim_dividend_paid_per_share and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == interim_dividend_paid_per_share and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == interim_dividend_paid_per_share and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の１株当たり当期純利益又は当期純損失
    def basicEarningsLossPershare_alone(self):
        try:
            tag_existence = self.search_existence_alone(basic_earnings_loss_pershare)
            if tag_existence == True:
                self.results += "単独決算　１株当たり当期純利益又は当期純損失（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == basic_earnings_loss_pershare and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value)) + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
     # 単体の潜在株式調整後１株当たり当期純利益
    def dilutedEarningsPershare_alone(self):
        try:
            tag_existence = self.search_existence_alone(diluted_earnings_pershare)
            if tag_existence == True:
                self.results += "単独決算　潜在株式調整後１株当たり当期純利益（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value)) + "\n"
                    elif fact.concept.qname.localName == diluted_earnings_pershare and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value)) + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の自己資本比率
    def equityToAssetRatio_alone(self):
        try:
            tag_existence = self.search_existence_alone(equity_to_asset_ratio)
            if tag_existence == True:
                self.results += "単独決算　自己資本比率（％）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == equity_to_asset_ratio and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_to_asset_ratio and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_to_asset_ratio and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_to_asset_ratio and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == equity_to_asset_ratio and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の自己資本利益率
    def rateOfReturnOnEquity_alone(self):
        try:
            tag_existence = self.search_existence_alone(rate_of_return_on_equity)
            if tag_existence == True:
                self.results += "単独決算　自己資本利益率（％）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == rate_of_return_on_equity and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == rate_of_return_on_equity and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == rate_of_return_on_equity and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == rate_of_return_on_equity and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == rate_of_return_on_equity and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の株価収益率
    def priceEarnigRatio_alone(self):
        try:
            tag_existence = self.search_existence_alone(price_earnigs_ratio)
            if tag_existence == True:
                self.results += "単独決算　株価収益率（％）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == price_earnigs_ratio and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == price_earnigs_ratio and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == price_earnigs_ratio and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == price_earnigs_ratio and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == price_earnigs_ratio and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

    # 単体の配当性向
    def payoutRatio_alone(self):
        try:
            tag_existence = self.search_existence_alone(payout_ratio)
            if tag_existence == True:
                self.results += "単独決算　配当性向（％）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == payout_ratio and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == payout_ratio and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == payout_ratio and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == payout_ratio and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == payout_ratio and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の営業活動によるキャッシュフロー
    def netCashProvidedByUsedInOperatingActivities_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_cach_provided_by_used_in_operatind_activities)
            if tag_existence == True:
                self.results += "単独決算　営業活動によるキャッシュフロー（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_cach_provided_by_used_in_operatind_activities and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_operatind_activities and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_operatind_activities and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_operatind_activities and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_operatind_activities and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の投資活動によるキャッシュフロー
    def netCashProvidedByUsedInInvestingActivities_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_cach_provided_by_used_in_investing_activities)
            if tag_existence == True:
                self.results += "単独決算　投資活動によるキャッシュフロー（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_cach_provided_by_used_in_investing_activities and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_investing_activities and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_investing_activities and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_investing_activities and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_investing_activities and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
     # 単体の財務活動によるキャッシュフロー
    def netCashProvidedByUsedInFinancingActivities_alone(self):
        try:
            tag_existence = self.search_existence_alone(net_cach_provided_by_used_in_financing_activities)
            if tag_existence == True:
                self.results += "単独決算　財務活動によるキャッシュフロー（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == net_cach_provided_by_used_in_financing_activities and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_financing_activities and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_financing_activities and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_financing_activities and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == net_cach_provided_by_used_in_financing_activities and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
        
    # 単体の現金及び現金同等物期末残高
    def cashAndCashEquivalents_alone(self):
        try:
            tag_existence = self.search_existence_alone(cash_and_cash_equivalents)
            if tag_existence == True:
                self.results += "単独決算　現金及び現金同等物期末残高（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == cash_and_cash_equivalents and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == cash_and_cash_equivalents and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == cash_and_cash_equivalents and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == cash_and_cash_equivalents and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == cash_and_cash_equivalents and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
     # 単体の株主総利回り
    def totalShareholderReturn_alone(self):
        try:
            tag_existence = self.search_existence_alone(total_sahre_holder_return)
            if tag_existence == True:
                self.results += "単独決算　株主総利回り（％）" + "\n"
                for fact in reversed(self.facts):         
                    if fact.concept.qname.localName == total_sahre_holder_return and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_sahre_holder_return and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_sahre_holder_return and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_sahre_holder_return and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(float(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == total_sahre_holder_return and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
    # 単体の従業員数
    def numberOfEmployees_alone(self):
        try:
            tag_existence = self.search_existence_alone(number_of_employees)
            if tag_existence == True:
                self.results += "単独決算　従業員数（名）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == number_of_employees and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == number_of_employees and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == number_of_employees and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == number_of_employees and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == number_of_employees and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

        # 単体の平均臨時雇用者数
    def averageNumberOfTemporaryWorkers_alone(self):
        try:
            tag_existence = self.search_existence_alone(average_number_of_temporary_workers)
            if tag_existence == True:
                self.results += "単独決算　平均臨時雇用者数（名）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == average_number_of_temporary_workers and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == average_number_of_temporary_workers and (fact.contextID == prior_1_alone or fact.contextID == prior_1_alone_instant):
                        self.results += f"{prior_1_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == average_number_of_temporary_workers and (fact.contextID == prior_2_alone or fact.contextID == prior_2_alone_instant):
                        self.results += f"{prior_2_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == average_number_of_temporary_workers and (fact.contextID == prior_3_alone or fact.contextID == prior_3_alone_instant):
                        self.results += f"{prior_3_year} :" + format(int(fact.value), ",") + "\n"
                    elif fact.concept.qname.localName == average_number_of_temporary_workers and (fact.contextID == prior_4_alone or fact.contextID == prior_4_alone_instant):
                        self.results += f"{prior_4_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
            # 単体の従業員平均年齢
    def averageAgeYears_alone(self):
        try:
            tag_existence = self.search_existence_alone(average_age_employees)
            if tag_existence == True:
                self.results += "単独決算　従業員平均年齢（歳）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == average_age_employees and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results

    # 単体の従業員平均勤続年数
    def averageLengthOfService_alone(self):
        try:
            tag_existence = self.search_existence_alone(average_length_of_service)
            if tag_existence == True:
                self.results += "単独決算　従業員平均勤続年数（年）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == average_length_of_service and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(float(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
            return None
        return self.results
    
        # 単体の平均年間給与
    def averageAnnualSalary_alone(self):
        try:
            tag_existence = self.search_existence_alone(average_annual_salary)
            if tag_existence == True:
                self.results += "単独決算　平均年間給与（円）" + "\n"
                for fact in reversed(self.facts):
                    if   fact.concept.qname.localName == average_annual_salary and (fact.contextID == prior_0_alone or fact.contextID == prior_0_alone_instant):
                        self.results += f"{prior_0_year} :" + format(int(fact.value), ",") + "\n"
            elif tag_existence == None:
                return None
        except:
             return None
        return self.results
    
    #上記すべてを実行するメソッド
    def select_all_info(self):
        self.companyName()
        self.netSales()
        self.ordinaryIncomeLoss()
        self.profitLoss()
        self.comprehensiveIncome()
        self.netAssets()
        self.totalAssets()
        self.netAssetsPershare()
        self.basicEarningsLossPershare()
        self.dilutedEarningsPershare()
        self.netSales_alone()
        self.ordinaryIncomeLoss_alone()
        self.profitLoss_alone()
        self.netIncomeLoss_alone()
        self.equityEarningLossEquityAlone()
        self.capitalStock_alone()
        self.comprehensiveIncome_alone()
        self.totalIssuedShare_alone()
        self.netAssets_alone()
        self.totalAssets_alone()
        self.netAssetsPershare_alone()
        self.dividendPaidShare_alone()
        self.interDividendPaidShare_alone()
        self.basicEarningsLossPershare_alone()
        self.dilutedEarningsPershare_alone()
        self.equityToAssetRatio_alone()
        self.rateOfReturnOnEquity_alone()
        self.priceEarnigRatio_alone()
        self.payoutRatio_alone()
        self.netCashProvidedByUsedInOperatingActivities_alone()
        self.netCashProvidedByUsedInInvestingActivities_alone()
        self.netCashProvidedByUsedInFinancingActivities_alone()
        self.cashAndCashEquivalents_alone()
        self.totalShareholderReturn_alone()
        self.numberOfEmployees_alone()
        self.averageNumberOfTemporaryWorkers_alone()
        self.averageAgeYears_alone()
        self.averageLengthOfService_alone()
        self.averageAnnualSalary_alone()
        return self.results

