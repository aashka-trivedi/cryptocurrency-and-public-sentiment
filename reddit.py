#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pmaw pandas


# In[1]:


import pandas as pd
from pmaw import PushshiftAPI
api = PushshiftAPI()


# In[2]:


import datetime as dt
before = int(dt.datetime(2021,2,1,0,0).timestamp())
after = int(dt.datetime(2020,12,1,0,0).timestamp())


# In[ ]:


subreddit="Bitcoin"
limit=500000 #Num of comments will be returned <=limit
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
print(f'Retrieved {len(comments)} comments from Pushshift')


# In[4]:


comments_df = pd.DataFrame(comments)
# preview the comments data
comments_df.head(5)


# In[5]:


comments_df.to_csv('./wsb_comments.csv', header=True, index=False, columns=list(comments_df.axes[1]))





