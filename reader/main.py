from flask import Flask, request, send_file, jsonify
import os
import json
from fu import sqlite_kv
from fu import json
from reader import config
from os import path

app = Flask(__name__, static_folder=path.join(path.dirname(__file__), '../front'), static_url_path='/')
db = sqlite_kv.SqliteCache(config.db_path)


@app.route("/api/get_article")
def get_article():
    article = request.args['article']
    res = db.query(article)
    return res


if __name__ == '__main__':
    app.debug = True
    app.run()
