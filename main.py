#!/anaconda3/bin/python3

from news_scraper import *
from statistical_classifier import *
# from api import *
from db import *
import datetime

if __name__ == "__main__":
	now = datetime.datetime.now()
	news = scrape_news()
	df = parse_news(news)
	create_table()
	df.to_sql('news_test', con, if_exists='append', index=False)
	con.commit()
	cur.close()
	con.close()
	print("Script completed at : ", now.strftime("%Y-%m-%d %H:%M:%S"))
