"""
利用book_list构建sqlite数据库

整个数据库是一个KV结构
books:是一个书籍列表
bookId=>书籍章节列表
文章Id=>文章详情
"""

from fu import sqlite_kv, json
from tqdm import tqdm

from reader import book_list
from reader import config
from os.path import exists, join
import os


class SqlitePut:
    def __init__(self):
        self.db = sqlite_kv.SqliteCache(config.db_path)

    def put(self, k, v):
        self.db.put(k, v)


class FilePut:
    def __init__(self):
        if not exists('gen'):
            os.mkdir('gen')

    def put(self, k, v):
        with open(join('gen', k), 'w') as f:
            f.write(v)


db = FilePut()
books = []
for b in tqdm(book_list.books, desc='正在构建数据库'):
    for part in b.parts:
        for art in part.articles:
            db.put(art.id, art.content)
            art.content = ""
    db.put(b.id, json.dumps(b, ensure_ascii=False))  # 把书籍内容及其章节存进去
    b.parts = []  # 清空parts
    books.append(b)
db.put("books", json.dumps(books, ensure_ascii=False))
