#Reference: https://medium.com/codex/10-best-resources-to-fetch-cryptocurrency-data-in-python-8400cf0d0136

import requests
import pandas as pd

def get_crypto_price(symbol, exchange, start_date = None, end_date=None):
    api_key = 'YOUR API KEY'
    api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={exchange}&apikey={api_key}'
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
    df = df.rename(columns = {'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low', '4a. close (USD)': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis = 1)
    if start_date:
        df = df[df.index >= start_date]
        if end_date:
            df = df[df.index <= end_date]
    return df

btc = get_crypto_price(symbol = 'BTC', exchange = 'USD', start_date = '2021-01-01', end_date='2021-08-31')

data_path = 'data/raw_bitcoin_price.csv'
btc.to_csv(data_path, sep='\t')

print(btc.head())
print(btc.tail())

