import os
import re
from os import path

from reader import book
from reader import config
from reader.log import logger

folder = path.join(config.ebook, '东野圭吾')


def get_parts(content: str):
    a = re.finditer('\n((\s*第[一二三四五六七八九十百千零0123456789]+[章回场](.+?)?)|(\s*[一二三四五六七八九十百千零0123456789]+\s*)|(\n.+?之章\s+[[一二三四五六七八九十]+\n))\n', content)
    splitters = book.get_pos(a)
    s = book.split_by_pos(content, splitters)
    arts = []
    for i in s:
        art = book.get_article(i)
        arts.append(art)
    p = book.Part()
    p.articles = arts
    return [p]


books = []
for i in os.listdir(folder):
    b = book.Book()
    b.name = i[:i.index('.')]
    b.author = '东野圭吾'
    b.tags = ['悬疑', '日本', '小说', '推理']
    logger.info(b.name)
    content = open(path.join(folder, i)).read()
    if '再生魔术之女' in i or '名侦探的规条' in i or '流星之绊' in i \
            or '怪笑小说' in i:
        book.set_book_with_articles([content], b)
        books.append(b)
        continue
    b.parts = get_parts(content)
    books.append(b)
if __name__ == '__main__':
    book.show_books(books)
