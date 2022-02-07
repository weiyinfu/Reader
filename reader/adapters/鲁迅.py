import os
import re
from os.path import *

from reader import config, book

luxun = join(config.ebook, "鲁迅")
a = os.listdir(luxun)
a = [i for i in a if i != '鲁迅目录.md']
mulu = open(join(luxun, '鲁迅目录.md')).read()
article = ['怀旧']
for line in mulu.splitlines():
    if '…' in line:
        title = line.strip()
        title = re.sub("[０-９Ａ-ＺA-Z]*…*$", "", title)
        title = re.sub("\s", "", title)
        article.append(title)
article_pattern = []
for i in article:
    p = '\s*'.join(i)
    p = f"{p}〔１〕"
    article_pattern.append(p)
title_pattern = "|".join(article_pattern)


def get_part(content):
    a = list(re.finditer(title_pattern, content))
    splitters = book.get_pos(a)
    s = book.split_by_pos(content, splitters)
    arts = []
    for ind, i in enumerate(s):
        art = book.Article()
        title = re.search(title_pattern, i)
        if title:
            title = title.group()
        else:
            lines = i.splitlines()
            for line in lines:
                if line.strip():
                    title = line.strip()
                    break
        title = re.sub('\s*', "", title)
        title = title.replace("〔１〕", "")
        art.name = title
        art.content = i
        arts.append(art)
    p = book.Part()
    p.articles = arts
    return p


books = []
for i in a:
    b = book.Book()
    b.name = i[i.index('-') + 1:i.index('.')]
    print(b.name)
    b.author = '鲁迅'
    books.append(b)
    content = open(join(luxun, i)).read()
    b.parts = [get_part(content)]
book.show_books(books)
