import json
import requests
import os
import time
import pandas
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
	for category, news in news_dict.items():
		# print("category: ", category)
		# print("news: ", news)
		source_name = news[0]['source']['name']
		source_id = news[0]['source']['id']
		title = news[0]['title']
		description = news[0]['description']
		url = news[0]['url']
		publishedAt = news[0]['publishedAt']
		content = news[0]['content']
		categ = category

		print("------------------")
		print("Category: ", categ)
		print("Published date: ", publishedAt)
		print("Source: ", source_name)
		print("Title: ", title)
		print("URL: ", url)
		print("Content: ", content)
		print("------------------")

if __name__ == "__main__":
	news = scrape_news()
	parsed_news = parse_news(news)
