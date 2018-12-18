from news_scraper import *
from statistical_classifier import *

if __name__ == "__main__":
	news = scrape_news()
	parsed_news = parse_news(news)