# cryptocurrency-and-public-sentiment

Repository for the class project for CSCI-GA 3033-065: Predictive Analytics. This project explores the relationship between public sentiment measured through Twitter tweets, Reddit networks and Google trends and the price of Bitcoin.

Collaborators: Aashka Trivedi, Minji Kim and Omkar Darekar

## Data Collection

All data has been collected for the time period 2021-01-01 to 2021-08-31. The datasets collected are:

1. Bitcoin Prices: Collected using the alpha-advantage api, and the script is in `raw_bitcoin_daily_prices.py`. Data collected is in `\data\bitcoin_price.csv`.
2. Google Trends: The daily google trends for the search term "bitcoin" is collected using the script `google_trends.py`, and the data is saved in `\data\google_trends_daily.csv`. Monthly interest over time from Januyary 2015 to January 2021 is saved in `google_trends.csv`. We use a constellation of terms to get the final dataset consisting of scaled search numbers for each term. This is done in `GoogleTrends.ipynb`, and the data is stored in `google_trends_daily_keywords.csv`.

## Data Preperation

1. Bitcoin Prices: the change in dialy price has been converted into categories, based on the analysis and script in `BitcoinPriceAnalysis.ipynb`. The price changed are converted into 5 categories:
    - -2 (Large Decrease in Price) : diff <-4000
    - -1 (Moderate Decrease in Price): -4000 <= diff < -500
    - 0 (No Commendable Difference) : -500 <= diff <= 500
    - 1 (Moderate Increase in Price): 500 < diff <= 4000
    - 2 (Large Increase in Price): 4000 < diff
The modified data is stored in `categorical_bitcoin_price.csv`
2. Google Search Trends: Since we use multiple keywords for the search numbers, we obtain a single daily search score by taking the average of the normalised search score for each keyword, and the weighted score for each keyword. The weighted score depends on how much the keyword is searched for on average. This data is stored in `trends_daily_score.csv`.  
3. Reddit Sentiment: To obtain a daily sentiment score, we use NLTK's `vader` library, to find the sentiment for each reddit comment. We then obtain a "daily" sentiment score by finding the average of the `compound` sentiments for all comments of that day. This is done in `RedditSentiment.ipynb`, and stored in `redditDailySentiment.csv`.

## Analysis

1. Granger Causality Analysis: first, we analyse whether Google Trends, Twitter Sentiment or Reddit Sentiment Granger Cause the differences in bitcoin prices. This analysis is done in `GrangerCausality.ipynb`.
2. Classification Model: we attempt to train a classifier to use twitter sentiment scores, reddit sentiment scores, and google trend scores to predict the category of change (highly negative to higlhly positive) of bitcoin prices. Experiments with different models are in `BitcoinPriceModel.ipynb`.

## Major Findings

1. Using the averaged google search score shows that google searches granger cause differences in bitcoin prices. Thus, we use the *averaged* google search score in all further analysis.
2. The average reddit sentiment per day is shown not to granger cause the Bitcoin Price changes.
