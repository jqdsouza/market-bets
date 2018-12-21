import json
import requests
import os
import time
import pandas as pd
from api_key import *

def scrape_news():
	categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
	news_dict = {}
	for category in categories:
		url = ('https://newsapi.org/v2/top-headlines?country=us&category={cat}&apiKey={key}').format(cat = category, key = API_KEY)
		response = requests.get(url)
		articles = response.json()['articles']
		news_dict[category] = articles
		# time.sleep(5) 

	return news_dict

def parse_news(news_dict):
	cols = ['source_name','source_id','title','description','url','publishedAt', 'content', 'category']
	df = pd.DataFrame(columns=cols)
	for category, news in news_dict.items():
		source_name = news[0]['source']['name']
		source_id = news[0]['source']['id']
		title = news[0]['title']
		description = news[0]['description']
		url = news[0]['url']
		publishedAt = news[0]['publishedAt']
		content = news[0]['content']
		categ = category
		curr_time = time.time()
		vals = [source_name, source_id, title, description, url, publishedAt, content, categ]
		df = df.append(pd.Series(vals, index=cols), ignore_index=True)

	df.to_csv(os.path.join('/Users/justin/desktop/personal/market-bets/output','news_{0}.csv'.format(curr_time)), index = False)

	return df
