import json
import requests
import os
import time
import pandas as pd
from api_key import *

def scrape_news():
	categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
	countries = ['us', 'ca'], #'ch', 'in', 'au', 'fr', 'ae', 'jp', 'de']
	news_dict = {}
	for category in categories:
		for country in countries:
			url = ('https://newsapi.org/v2/top-headlines?country={country}&category={cat}&apiKey={key}').format(country = country, cat = category, key = API_KEY)
			response = requests.get(url)
			articles = response.json()['articles']
			news_dict[category] = articles
		# time.sleep(5) 

	return news_dict

def parse_news(news_dict):
	cols = ['source_name','source_id','title','description','url','publishedAt', 'content', 'category']
	global_df = pd.DataFrame(columns=cols)
	for category, news in news_dict.items():
		for news_item in news:
			# data = json.dumps(news_item)
			# testy_df = pd.read_json(data)
			source_name = news_item['source']['name']
			source_id = news_item['source']['id']
			title = news_item['title']
			description = news_item['description']
			url = news_item['url']
			publishedAt = news_item['publishedAt']
			content = news_item['content']
			categ = category
			vals = [source_name, source_id, title, description, url, publishedAt, content, categ]
			temp_df = pd.Series(vals, index=cols)
			global_df = global_df.append(temp_df, ignore_index = True)

	curr_time = time.time()
	global_df.to_csv(os.path.join('/Users/justin/desktop/personal/market-bets-data/news','news_{0}.csv'.format(curr_time)), index = False)

	return global_df
