"""
利用book_list构建sqlite数据库
"""

from reader import book_list
from fu import sqlite_kv, snow_flake, json
from tqdm import tqdm
from reader import config

index = []
db = sqlite_kv.SqliteCache(config.db_path)
snow = snow_flake.SnowFlake()


def put(article: str):
    i = str(snow.get_id())
    db.put(i, article)
    return i


for b in tqdm(book_list.books, desc='正在构建数据库'):
    for part in b.parts:
        for art in part.articles:
            art.content = put(art.content)
json.dump(book_list.books, config.index_path, indent=2)
