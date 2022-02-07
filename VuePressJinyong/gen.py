import json
import os
from os.path import *

from reader import book_list
from reader.book import Book


def write(filepath, filecontent):
    if not exists(dirname(filepath)):
        os.makedirs(dirname(filepath))
    with open(filepath, mode='w') as f:
        lines = filecontent.split('\n')
        filecontent = '\n'.join([i + '  ' for i in lines])
        f.write(filecontent)


Sidebar = {}
for book in book_list.books:
    book: Book = book
    if book.author not in ('毛泽东', '金庸'):
        continue
    pa = ['docs/gen', book.author, book.name]
    if len(book.parts) > 1:
        print(f"忽略有多个part的书籍{book.name} {book.author}")
    p = book.parts[0]
    sidebar = []
    for ind, art in enumerate(p.articles):
        filepath = join(*pa, f"{ind}.md")
        write(filepath, art.content)
        sidebar.append((art.name, filepath))
    sb = []
    for title, path in sidebar:
        sb.append({'title': title, 'path': '/' + relpath(path, "docs")})
    Sidebar['/' + relpath(join(*pa), "docs")] = sb
    indexMd = []
    for title, path in sidebar:
        indexMd.append(f"* [{title}]({'/' + relpath(path, 'docs')})  ")
    open(join(*pa, 'index.md'), 'w').write('\n'.join(indexMd))

json.dump(Sidebar, open('docs/.vuepress/catelog.json', 'w'), indent=2, ensure_ascii=False)
