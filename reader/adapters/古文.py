import os
import re
from os.path import *

from fu import json

from reader import book
from reader import config

a = join(config.ebook, '古文/src')
b = book.Book()
b.name = '古文'
b.author = ''
b.parts = []
b.tags = ['古文']
p = book.Part()
p.name = '古文'
for i in os.listdir(a):
    if i == 'SUMMARY.md':
        continue
    name = re.search('\d+-(.+)\.md', i).group(1)
    art = book.Article()
    art.name = name
    art.content = open(join(a, i)).read()
    p.articles.append(art)
b.parts.append(p)
a = json.load(join(config.ebook, '古文/guwen.json'))


def get_content(x):
    other = []
    for i in x:
        if i not in ('title', 'author', 'content'):
            other.append(i)
            other.append(str(x[i]))
    o = '\n'.join(other)
    content = x['content']
    if type(content) == list:
        content = '\n'.join(content)
    return f"""{x['title']}  {x.get('author')}
{content}
{o}
"""


for i in a:
    art = book.Article()
    art.name = i['title']
    art.content = get_content(i)
    p.articles.append(art)
books = [b]

if __name__ == '__main__':
    print(books)
