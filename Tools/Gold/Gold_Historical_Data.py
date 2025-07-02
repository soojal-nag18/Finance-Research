import yfinance as yf
import pandas as pd
from datetime import datetime

today = datetime.today().strftime('2025-07-01') #can modify to your own date as per need.

gold = yf.download('GLD', start='2005-01-01', end=today, interval='1d', auto_adjust=True)
usd_inr = yf.download('INR=X', start='2005-01-01', end=today, interval='1d', auto_adjust=True)

if gold.empty or usd_inr.empty:
    print("Download failed. Try adjusting ticker or date range.")  #error (change dates is error occur, might happen due to lack of data for specific date. )
else:
    data = pd.DataFrame()
    data['Gold_USD'] = gold['Close']
    data['USD_INR'] = usd_inr['Close']
    data.dropna(inplace=True)
    data['Gold_INR'] = data['Gold_USD'] * data['USD_INR']
    data['Gold_INR_per_gram'] = data['Gold_INR'] / 31.1035

    data.to_csv('gold_inr_history.csv')    #saves data extracted to csv file
    print(f"Saved gold_inr_history.csv with {len(data)} rows.")
