
import pymysql.cursors

class sample_db:
        
    def sample(self,user_id):
        connect = pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )
        try:
            cursor = connect.cursor()
            sql = f"SELECT COUNT(*) FROM Talk WHERE user_id = '{user_id}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0] 

        finally:
            cursor.close()
            connect.commit()
            connect.close()
            print('Complete!')
        
    #最低限のデータベース作る
    def make_db(self):
        connect = pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )
        try:
            cursor = connect.cursor()
            sql_1 = "create table if not exists Talk(talk_id int auto_increment primary key, user_id char(50), user_text varchar(1000) not null,ai_text varchar(1000) not null)"
            cursor.execute(sql_1)
            sql_2 = "create table if not exists Company_Discriptions(company_name char(50) primary key not null, company_dis varchar(1000), created_at TIMESTAMP)"
            cursor.execute(sql_2)
            sql_3 = "create table if not exists Company_Analysis(company_name char(50) primary key not null, company_dis varchar(1000), created_at TIMESTAMP)"
            cursor.execute(sql_3)

        finally:
            cursor.close()
            connect.commit()
            connect.close()
            
        print('Complete!')
        
    def text_to_db(self,user_id,user_text,ai_text):
        connect = pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )
        try:
            cursor = connect.cursor()
            sql = f"insert into Talk (user_id,user_text,ai_text) value ('{user_id}','{user_text}','{ai_text}')"
            cursor.execute(sql)

        finally:
            cursor.close()
            connect.commit()
            connect.close()
        print('Complete!')
        
    def company_dis_to_db(self,company_name,company_dis):
        connect = pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )
        try:
            cursor = connect.cursor()
            sql = f"insert into Company_Discriptions (company_name,company_dis) value ('{company_name}','{company_dis}')"
            cursor.execute(sql)

        finally:
            cursor.close()
            connect.commit()
            connect.close()
        print('Complete!')
    
    def company_ana_to_db(self,company_name,company_ana):
        connect = pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )
        try:
            cursor = connect.cursor()
            sql = f"insert into Company_Analysis (company_name,company_dis) value ('{company_name}','{company_ana}')"
            cursor.execute(sql)

        finally:
            cursor.close()
            connect.commit()
            connect.close()
        print('Complete!')
        
    def fetch_company_dis(self,company_name):
        connect =pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )

        try:
            # カーソルを作成
            cursor = connect.cursor()
            
            # Company_Discriptionsテーブルから、company_name列がある企業名である行を検索
            sql = "SELECT company_dis FROM Company_Discriptions WHERE company_name = %s"
            cursor.execute(sql, (company_name))

            # 結果を取得
            result = cursor.fetchone()
            
            if result is not None:
                company_dis = result[0]
                return company_dis
            else:
                return None
        finally:
            # カーソルと接続を閉じる
            cursor.close()
            connect.close()
    
    def fetch_company_ana(self,company_name):
        connect =pymysql.connect(
            user='root',
            passwd='Orange0912',
            host='localhost',
            db='sample_db'
        )

        try:
            # カーソルを作成
            cursor = connect.cursor()
            
            # Company_Discriptionsテーブルから、company_name列がある企業名である行を検索
            sql = f"SELECT company_dis FROM Company_Analysis WHERE company_name = {company_name}"
            cursor.execute(sql)
            
            # 結果を取得
            result = cursor.fetchone()
            
            # 結果がある場合、変数Xに値を代入
            if result is not None:
                company_dis = result[0]
                return company_dis
            else:
                return None
        finally:
            # カーソルと接続を閉じる
            cursor.close()
            connect.close()

# db = sample_db()
# res = db.sample(user_id='Ua388147c2aaeecb75635d96f4f30bf05')
# print(res)


        
        






