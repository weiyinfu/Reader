import os
import re
from os import path

from reader import book
from reader import config
from reader.log import logger

folder = path.join(config.ebook, '金庸/金庸全集三联版')
"""
金庸小说：越女剑、鸳鸯刀比较简短
"""


def split_book(content: str):
    assert '后记' in content
    beg = re.search('后记\s*\n', content).start()
    main = content[:beg]
    res = re.finditer("第[1234567890一二三四五六七八九十]+[章回]\s+.+?\n", main)
    splitters = book.get_pos(res)
    if not splitters:
        res = re.finditer("[一二三四五六七八九十零]+\s.*?\n", main)
        splitters = book.get_pos(res)
    splitters.append(beg)
    return book.split_by_pos(content, splitters)


def parse_folder():
    books = []
    for i in os.listdir(folder):
        if i.endswith('.txt'):
            name = i[:-4]
            b = book.Book()
            b.name = name
            b.author = '金庸'
            b.tags = ['武侠', '金庸']
            filepath = path.join(folder, i)
            content = open(filepath).read()
            logger.info(b.name)
            if '鸳鸯刀' in i or '白马啸西风' in i:
                book.set_book_with_articles([content], b)
                books.append(b)
                continue
            articles = split_book(content)
            book.set_book_with_articles(articles, b)
            books.append(b)
    return books


books = parse_folder()
if __name__ == '__main__':
    book.show_books(books)
