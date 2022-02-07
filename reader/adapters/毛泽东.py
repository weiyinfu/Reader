from os import path

import os

from reader import config, book
import re

"""
毛泽东文集是一个MARKDOWN格式的repo
"""
folder = path.join(config.ebook, '毛泽东文集/src')

arts = []
for i in sorted(os.listdir(folder)):
    if not re.match('^\d+-', i):
        continue
    art = book.Article()
    art.name = i[:i.index('.')]
    art.content = open(path.join(folder, i)).read()
    arts.append(art)
p = book.Part()
p.name = '毛泽东文集'
p.articles = arts
b = book.Book()
b.author = '毛泽东'
b.name = '毛泽东文集'
b.parts = [p]
b.tags = ['毛泽东', '文集', '马克思主义']
books = [b]

if __name__ == '__main__':
    print(len(books))
    print(books)
