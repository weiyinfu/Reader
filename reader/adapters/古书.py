from os.path import *

from reader import config, book

gushu = join(config.ebook, '古书')


def get_book(name: str):
    content = open(join(gushu, name + ".txt")).read()
    b = book.Book()
    b.name = name
    b.tags = ['古书']
    p = book.Part()
    p.name = name
    art = book.Article()
    art.name = name
    art.content = content
    p.articles = [art]
    b.parts = [p]
    return b


weiru = get_book("围炉夜话")
shenglv = get_book("声律启蒙")
liweng = get_book('笠翁对韵')
laozi = get_book("老子")

books = [weiru, shenglv, liweng, laozi]
