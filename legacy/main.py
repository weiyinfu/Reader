import json
from os import path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fu import sqlite_kv

from reader import config

app = FastAPI()
db = sqlite_kv.SqliteCache(config.db_path)
cur_dir = path.dirname(__file__)
static_folder = path.join(cur_dir, "../front/dist")
app.mount("/static", StaticFiles(directory=static_folder), name="static")


@app.get("/api/get_article")
def get_article(article: int):
    # 获取章节内容
    resp = db.query(article)
    return resp


@app.get("/api/book_list")
def get_book_list():
    # 获取书籍列表
    return json.loads(db.query('books'))


@app.get("/api/book_info")
def get_book_info(book_id: str):
    # 获取书籍详情，主要是目录
    return json.loads(db.query(book_id))


if __name__ == '__main__':
    uvicorn.run(app)
