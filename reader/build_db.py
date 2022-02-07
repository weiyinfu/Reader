import json
import os
from os.path import exists, join

from tqdm import tqdm

from reader import book_list


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
