# cryptocurrency-and-public-sentiment

Repository for the class project for CSCI-GA 3033-065: Predictive Analytics. This project explores the relationship between public sentiment measured through Twitter tweets, Reddit networks and Google trends and the price of Bitcoin.

Collaborators: Aashka Trivedi, Minji Kim and Omkar Darekar

## Data Collection

All data has been collected for the time period 2021-01-01 to 2021-08-31. The datasets collected are:

1. Bitcoin Prices: Collected using the alpha-advantage api, and the script is in `raw_bitcoin_daily_prices.py`. Data collected is in `\data\bitcoin_price.csv`.
2. Google Trends: The daily google trends for the search term "bitcoin" is collected using the script `google_trends.py`, and the data is saved in `\data\google_trends_daily.csv`. Monthly interest over time from Januyary 2015 to January 2021 is saved in `google_trends.csv`. We use a constellation of terms to get the final dataset consisting of scaled search numbers for each term. This is done in `GoogleTrends.ipynb`, and the data is stored in `google_trends_daily_keywords.csv`. Normalized daly scores for all keywords are stored in `trends_daily_score.csv`

## Data Preperation

1. Bitcoin Prices: the change in dialy price has been converted into categories, based on the analysis and script in `BitcoinPriceAnalysis.ipynb`. The price changed are converted into 5 categories:
    - -2 (Large Decrease in Price) : diff <-4000
    - -1 (Moderate Decrease in Price): -4000 <= diff < -500
    - 0 (No Commendable Difference) : -500 <= diff <= 500
    - 1 (Moderate Increase in Price): 500 < diff <= 4000
    - 2 (Large Increase in Price): 4000 < diff
The modified data is stored in `categorical_bitcoin_price.csv`
