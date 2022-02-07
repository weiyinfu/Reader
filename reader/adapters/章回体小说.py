from reader import config, book

import os
from os.path import *
import re
from reader.log import logger

folder = join(config.ebook, '网络小说')
novels = []
novels.extend([join(folder, i) for i in os.listdir(folder)])
folder = join(config.ebook, '四大名著/src')
novels.extend([join(folder, i) for i in os.listdir(folder)])
folder = join(config.ebook, '茅盾文学奖')
novels.extend([join(folder, i) for i in os.listdir(folder)])

books = []
authors = {
    '亮剑': ('都梁', ['网络小说', '当代']),
    '欢喜债': ('笑佳人', ['网络小说', '当代']),
    '何以笙箫默': ('顾漫', ['网络小说', '当代']),
    '斗罗大陆': ('唐家三少', ['网络小说', '当代']),
    '斗罗大陆2': ('唐家三少', ['网络小说', '当代']),
    '斗罗大陆4终极斗罗': ('唐家三少', ['网络小说', '当代']),
    '水浒传': ('施耐庵', ['四大名著', '古典文学']),
    '水浒全传': ('施耐庵', ['四大名著', '古典文学']),
    '三国演义': ('罗贯中', ['四大名著', '古典文学']),
    '红楼梦': ('曹雪芹', ['四大名著', '古典文学']),
    '西游记': ('吴承恩', ['四大名著', '古典文学']),
    '平凡的世界': ('路遥', ['茅盾文学奖', '当代文学', ]),
    '白鹿原': ('陈忠实', ['茅盾文学奖', '当代文学']),
}


def get_parts(content: str):
    a = re.finditer('\n\s*第[零一二三四五六七八九十百千1234567890]+[章回](.+?)?\n', content)
    splitters = book.get_pos(a)
    s = book.split_by_pos(content, splitters)
    arts = []
    for i in s:
        art = book.get_article(i)
        arts.append(art)
    p = book.Part()
    p.articles = arts
    return [p]


for filepath in novels:
    b = book.Book()
    filename = basename(filepath)
    b.name = filename[:filename.index('.')]
    b.author, b.tags = authors[b.name]
    logger.info(b.name)
    b.parts = get_parts(open(filepath).read())
    books.append(b)

if __name__ == '__main__':
    book.show_books(books)
