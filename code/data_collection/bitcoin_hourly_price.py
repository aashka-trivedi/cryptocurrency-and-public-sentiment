#Bitcoin Prices taken from https://www.cryptodatadownload.com/cdd/Bitstamp_BTCUSD_1h.csv
import pandas as pd


btc_raw = pd.read_csv('../../data/bitcoin_hourly_raw.csv', sep=',', index_col=None)
#drop Unix and Symbol columns
btc = btc_raw.drop(['unix', 'symbol'], axis = 1)

btc.to_csv('../../data/bitcoin_hourly.csv', sep=",", index=False)
