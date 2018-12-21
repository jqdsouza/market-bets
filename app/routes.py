from __init__ import *
import flask
import json
from flask import request, jsonify
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Market Bets</h1><p>This site is for degenerates who want to gamble away their life savings.</p>"

@app.route('/news/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('news.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_news = cur.execute('SELECT * FROM news_test;').fetchall()
    #response = json.dumps(all_news, sort_keys = True, indent = 4, separators = (',', ': '))
    response = jsonify(all_news)

    return response

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/news/', methods=['GET'])
def api_filter():
    query_parameters = request.args

    category = query_parameters.get('category')
    publishedAt = query_parameters.get('publishedAt')
    title = query_parameters.get('title')

    query = "SELECT * FROM news_test WHERE"
    to_filter = []

    if category:
        query += ' category=? AND'
        to_filter.append(category)
    if publishedAt:
        query += ' publishedAt=? AND'
        to_filter.append(publishedAt)
    if title:
        query += ' title=? AND'
        to_filter.append(title)
    if not (category or publishedAt or title):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('news.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    response = jsonify(results)

    return response


