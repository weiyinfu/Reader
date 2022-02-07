import os
import re
from os import path

from reader import book
from reader import config
from reader.log import logger

folder = path.join(config.ebook, '琼瑶')


def get_parts(book_name, content: str):
    if book_name in ['望夫崖']:
        a = list(re.finditer("(?:^|\n)[１２３４５６７８９０]+．.+?\n", content))
    elif book_name in ['我的故事', '剪不断的乡愁']:
        a = list(re.finditer("(?:^|\n)[一二三四五六七八九十百千零]+\s*、.+?\n", content))
    elif book_name in ['还珠格格']:
        a = list(re.finditer("(?:^|\n)第\s*[一二三四五六七八九十百千零]+\s*章.+?\n", content))
    else:
        a = list(re.finditer('((?:^|\n)\d+\s*\n)|((?:^|\n)[１２３４５６７８９０]+\s*\n)|((?:^|\n)[一二三四五六七八九十百千零]+\s*\n)', content))
    splitters = book.get_pos(a)
    # print(splitters, a)
    s = book.split_by_pos(content, splitters)
    arts = []
    for ind, i in enumerate(s):
        art = book.Article()
        lines = i.splitlines()
        for line in lines:
            if line.strip():
                art.name = line.strip()
                break
        art.content = i
        arts.append(art)
    p = book.Part()
    p.articles = arts
    return [p]


books = []
for i in os.listdir(folder):
    print(i)
    b = book.Book()
    b.name = i[:i.index('.')]
    b.author = '琼瑶'
    b.tags = ['言情', '小说']
    logger.info(b.name)
    content = open(path.join(folder, i)).read()
    b.parts = get_parts(b.name, content)
    books.append(b)
if __name__ == '__main__':
    book.show_books(books)
