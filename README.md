# cryptocurrency-and-public-sentiment

Repository for the class project for CSCI-GA 3033-065: Predictive Analytics. This project explores the relationship between public sentiment measured through Twitter tweets, Reddit networks and Google trends and the price of Bitcoin.

Collaborators: Aashka Trivedi, Minji Kim and Omkar Darekar

## Data Collection

All data has been collected for the time period 2021-01-01 to 2021-08-31. The datasets collected are:

1. Bitcoin Prices: Collected using the alpha-advantage api, and the script is in `raw_bitcoin_daily_prices.py`. Data collected is in `\data\bitcoin_price.csv`.
2. Google Trends: The daily google trends for the search term "bitcoin" is collected using the script `google_trends.py`, and the data is saved in `\data\google_trends_daily.csv`. Monthly interest over time from Januyary 2015 to January 2021 is saved in `google_trends.csv`. We use a constellation of terms to get the final dataset consisting of scaled search numbers for each term. This is done in `GoogleTrends.ipynb`, and the data is stored in `google_trends_daily_keywords.csv`.
3. Reddit data: The reddit data is scrapped by using Pushshift API which enables collection of large amounts of Reddit data. The executing file is Reddit_scrapDataset.ipynb,  and the row data will be saved in `./wsb_comments.csv`. Afterwards, the data which only includes columns (Comments and its date) that we needed is saved in `./reddit_dataset.csv`.

## Data Preperation

### Daily Analysis

1. Bitcoin Prices: the change in dialy price has been converted into categories, based on the analysis and script in `BitcoinPriceAnalysis.ipynb`. The price changed are converted into 5 categories:
    - -2 (Large Decrease in Price) : diff <-4000
    - -1 (Moderate Decrease in Price): -4000 <= diff < -500
    - 0 (No Commendable Difference) : -500 <= diff <= 500
    - 1 (Moderate Increase in Price): 500 < diff <= 4000
    - 2 (Large Increase in Price): 4000 < diff
The modified data is stored in `data/daily_data/categorical_bitcoin_price.csv`
2. Google Search Trends: Since we use multiple keywords for the search numbers, we obtain a single daily search score by taking the average of the normalised search score for each keyword, and the weighted score for each keyword. The weighted score depends on how much the keyword is searched for on average. This data is stored in `data/daily_data/trends_daily_score.csv`.  
3. Reddit Sentiment: To obtain a daily sentiment score, we use NLTK's `vader` library, to find the sentiment for each reddit comment. We then obtain a "daily" sentiment score by finding the average of the `compound` sentiments for all comments of that day. This is done in `RedditSentiment.ipynb`, and stored in `data/daily_data/redditDailySentiment.csv`.
4. Twitter Sentiment: We follow the same methodology to calculate the daily/hourly Twitter Sentiment as followed by Reddit. We use NLTK's Vader library to assign a daily/ hourly sentiment score  for a given day for a 8 month period.

### Hourly Analysis

1. Bitcoin Prices: the change in hourly price has been converted into categories, based on the analysis and script in `BitcoinPriceAnalysis.ipynb`. The price changed are converted into 3 categories:
    - -1 (Decrease in Price):  diff < -150
    - 0 (No Commendable Difference) : -150 <= diff <= 150
    - 1 (Increase in Price): 150 < diff 
The modified data is stored in `data/hourly_data/categorical_bitcoin_hourly.csv`
2. Google Search Trends: Since we use multiple keywords for the search numbers, we obtain a single hourly search score by taking the average of the normalised search score for each keyword, and the weighted score for each keyword. The weighted score depends on how much the keyword is searched for on average. This data is stored in `data/hourly_data/trends_hourly_score.csv`.  Please note that google trends can only be found on a per-day granularity, so to obtain hourly data, the daily value is replicated over a 24 hour period.
3. Reddit Sentiment: To obtain a daily sentiment score, we use NLTK's `vader` library, to find the sentiment for each reddit comment. We then obtain a "hourly" sentiment score by finding the average of the `compound` sentiments for all comments of that hour. This is done in `RedditSentiment.ipynb`, and stored in `data/hourly_data/redditHourlySentiment.csv`.
4. Twitter Sentiment: Following the same method to calculate daily scores, we improve the granularity of the data set by assigning an hourly score for tweets so we have a larger data feed into the model. We use NLTK's Vader library to find a compound score for each hour for an 8 month time period.

## Analysis

1. Granger Causality Analysis: first, we analyse whether Google Trends, Twitter Sentiment or Reddit Sentiment Granger Cause the differences in bitcoin prices. This analysis is done in `GrangerCausality.ipynb`.
2. Classification Model: we attempt to train a classifier to use twitter sentiment scores, reddit sentiment scores, and google trend scores to predict the category of change (highly negative to higlhly positive) of bitcoin prices. Experiments with different models are in `BitcoinPriceModel.ipynb`.

## Major Findings

### Daily Analysis

1. Using the averaged google search score shows that google searches granger cause differences in bitcoin prices. Thus, we use the *averaged* google search score in all further analysis.
2. The average reddit sentiment per day is shown not to granger cause the Bitcoin Price changes.
3. The average twitter sentiment per day is shown to strongly granger cause the Bitcoin Price changes.
4. The best predictive model on a daily granularity is a Random Forest Classifier, which achieves a 56.6% accuracy after hyperparamter optimization.

### Hourly Analysis

1. Using the averaged google search score shows that google searches strongly granger cause differences in bitcoin prices.
2. The average reddit sentiment per hour is shown not to granger cause the Bitcoin Price changes.
3. The average twitter sentiment per hour is shown to strongly granger cause the Bitcoin Price changes.
4. The best predictive model on a daily granularity is a Decision Tree Classifier, which achieves a 58.7% accuracy after hyperparamter optimization.
