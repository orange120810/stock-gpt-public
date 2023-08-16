from pandas_datareader import data
import json
import os
import pandas as pd 
import numpy as np

class technical_data:

    def __init__(self,code):
        self.code = code
        # 株価データを取得
        self.df = data.DataReader(f'{self.code}.JP', 'stooq')
        self.df.sort_index(inplace=True)
        self.df = self.df.tail(50)

    def SMA(self):
        self.df["SMA5"] = self.df["Close"].rolling(window=5).mean()
        self.df["SMA25"] = self.df["Close"].rolling(window=25).mean()
        return self.df
    
    def macd(self):
        FastEMA_period = 12 # 短期EMAの期間
        SlowEMA_period = 26 # 長期EMAの期間
        SignalSMA_period = 9 # SMAを取る期間
        self.df["MACD"] = self.df["Close"].ewm(span=FastEMA_period).mean() - self.df["Close"].ewm(span=SlowEMA_period).mean()
        self.df["Signal"] = self.df["MACD"].rolling(SignalSMA_period).mean()
        return self.df
    
    def rsi(self):
        # 前日との差分を計算
        df_diff = self.df["Close"].diff(1)
    
        # 計算用のDataFrameを定義
        df_up, df_down = df_diff.copy(), df_diff.copy()
        
        # df_upはマイナス値を0に変換
        # df_downはプラス値を0に変換して正負反転
        df_up[df_up < 0] = 0
        df_down[df_down > 0] = 0
        df_down = df_down * -1
        
        # 期間14でそれぞれの平均を算出
        df_up_sma14 = df_up.rolling(window=14, center=False).mean()
        df_down_sma14 = df_down.rolling(window=14, center=False).mean()
    
        # RSIを算出
        self.df["RSI"] = 100.0 * (df_up_sma14 / (df_up_sma14 + df_down_sma14))
    
        return self.df
    
    def SMA_macd_RSI(self):
        #SMA
        self.df["SMA5"] = self.df["Close"].rolling(window=5).mean()
        self.df["SMA25"] = self.df["Close"].rolling(window=25).mean()
        #macd
        FastEMA_period = 12 # 短期EMAの期間
        SlowEMA_period = 26 # 長期EMAの期間
        SignalSMA_period = 9 # SMAを取る期間
        self.df["MACD"] = self.df["Close"].ewm(span=FastEMA_period).mean() - self.df["Close"].ewm(span=SlowEMA_period).mean()
        self.df["Signal"] = self.df["MACD"].rolling(SignalSMA_period).mean()
        #RSI
        df_diff = self.df["Close"].diff(1)
        # 計算用のDataFrameを定義
        df_up, df_down = df_diff.copy(), df_diff.copy() 
        # df_upはマイナス値を0に変換
        # df_downはプラス値を0に変換して正負反転
        df_up[df_up < 0] = 0
        df_down[df_down > 0] = 0
        df_down = df_down * -1
        
        # 期間14でそれぞれの平均を算出
        df_up_sma14 = df_up.rolling(window=14, center=False).mean()
        df_down_sma14 = df_down.rolling(window=14, center=False).mean()
    
        # RSIを算出
        self.df["RSI"] = 100.0 * (df_up_sma14 / (df_up_sma14 + df_down_sma14))

        return self.df






