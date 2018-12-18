import csv, sqlite3
import pandas as pd

con = sqlite3.connect("news.db")
cur = con.cursor()

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS news_test (source_name TEXT, source_id TEXT, title TEXT, description TEXT, url TEXT, publishedAt TEXT, content TEXT, category TEXT);") # use your column names here

# def dynamic_data_entry():
# 	cur.execute("INSERT INTO news_test (source_name, source_id, title, description, url, publishedAt, content, category) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", )

