import requests
from bs4 import BeautifulSoup

company_code = 1301

class scraping_all_info:

    def __init__(self,code):
        self.code = code
        self.info = []

    def scraping_prime(self):
        try:
            url = f'https://www.traders.co.jp/stocks/61_{self.code}/'
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            th = soup.find_all("th")
            td = soup.find_all("td")
            span = soup.find_all("span")

            for i in range(11):
                self.info.append(str(th[15+i].contents[0]) + ":" + str(td[20+i].contents[0]))

            for i in range(3):
                self.info.append(str(th[26+i].contents[0]) + ":" + str(span[19+i].contents[0]))
            
            return self.info
        
        except Exception as e:
            return e

    def scraping_standard(self):
        try:
            url = f'https://www.traders.co.jp/stocks/62_{self.code}/'
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            th = soup.find_all("th")
            td = soup.find_all("td")
            span = soup.find_all("span")

            self.info.append(("現在値："+ str(span[10:15]).contents[0]))

            for i in range(11):
                self.info.append(str(th[15+i].contents[0]) + ":" + str(td[20+i].contents[0]))

            for i in range(3):
                self.info.append(str(th[26+i].contents[0]) + ":" + str(span[19+i].contents[0]))
            return self.info
        except:
            None

    def scraping_growth(self):
        try:
            url = f'https://www.traders.co.jp/stocks/63_{self.code}/'
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            th = soup.find_all("th")
            td = soup.find_all("td")
            span = soup.find_all("span")

            self.info.append(("現在値："+ str(span[14].contents[0])))

            for i in range(11):
                self.info.append(str(th[15+i].contents[0]) + ":" + str(td[20+i].contents[0]))

            for i in range(3):
                self.info.append(str(th[26+i].contents[0]) + ":" + str(span[19+i].contents[0]))
            return self.info
        except:
            None
    
    def scraping(self):
        try:
            res_prime = self.scraping_prime()
            result = '\n'.join(res_prime)
            return result
        except:
            try:
                res_standerd = self.scraping_standard()
                result = '\n'.join(res_standerd)
                return result
            except:
                try:
                    res_groth = self.scraping_growth()
                    result = '\n'.join(res_groth)
                    return result
                except:
                    result = "取得できませんでした"
                    return result
    
    def scraping_prime_now(self):
        try:
            url = f'https://www.traders.co.jp/stocks/61_{self.code}/'
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")
            span = soup.find_all("span")

            now_price = "現在値：" + str(span[14].contents[0]+"円")
            return now_price
        except:
            None
    
    def scraping_standard_now(self):
        try:
            url = f'https://www.traders.co.jp/stocks/62_{self.code}/'
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")
            span = soup.find_all("span")

            now_price = "現在値：" + str(span[14].contents[0]+"円")
            return now_price
        except:
            None
    
    def scraping_growth_now(self):
        try:
            url = f'https://www.traders.co.jp/stocks/63_{self.code}/'
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")
            span = soup.find_all("span")

            now_price = "現在値：" + str(span[14].contents[0]+"円")
            return now_price
        except:
            None
    
    def scraping_now_price(self):
        res_prime = self.scraping_prime_now()
        if res_prime != None:
            return res_prime
        elif res_prime == None:
            res_standerd = self.scraping_standard_now()
            if res_standerd != None:
                return res_standerd
            elif res_standerd == None:
                res_growth = self.scraping_growth_now()
                if res_growth != None:
                    return res_growth
                else:
                    None
 



        




