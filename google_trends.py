#PyTrends Documentation: https://github.com/GeneralMills/pytrends
#Reference: http://www.easy2digital.com/automation/data/python-tutorial-for-digital-marketers-9-big-picture-matters-how-to-pull-data-from-google-trends-api-via-pytrends/


import pandas as pd                        
from pytrends.request import TrendReq

#Connect to Google 
pytrends = TrendReq()

#Get Interest over time 
keywords = ['bitcoin']
#IMPORTANT: Use specific timeframe- using "now" or "today" throws a 400 error
pytrends.build_payload(kw_list=keywords, cat=0, timeframe='2015-01-01 2021-01-01', geo='', gprop='')
interest_data = pytrends.interest_over_time()

#Format Dataframe
interest_data = interest_data.reset_index()
interest_data = interest_data.drop(['isPartial'], axis=1)

#Spot Check
print(interest_data.head())

#Save Data
data_path = 'data/google_trends.csv'
interest_data.to_csv(data_path, sep='\t')

