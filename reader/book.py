import re
from typing import List, Iterable

from fu import snow_flake
from fu.dict_obj import DictObj

"""
book结构体定义+一些电子书解析函数

一个Book包含多个Part，一个Part包含多个Article
"""
snow = snow_flake.SnowFlake()


class Article(DictObj):
    def __init__(self):
        super().__init__()
        self.id = str(snow.get_id())
        self.name = ""
        self.content = ''  # 这是最终的内容


class Part(DictObj):
    def __init__(self):
        super().__init__()
        self.id = str(snow.get_id())
        self.name = ""
        self.articles: List[Article] = []  # 一个部分是由若干个课文组成的


class Book(DictObj):
    def __init__(self):
        super().__init__()
        self.id = str(snow.get_id())
        self.name = 'book'
        self.author = 'author'
        self.tags: List[str] = []  # 书籍的标签
        self.parts: List[Part] = []  # 书籍的部分


def get_article(s: str) -> Article:
    # 根据文章内容创建一个Article对象
    ar = Article()
    ar.name = s.strip().splitlines()[0]  # 以第一行为题目
    if len(ar.name) > 30:
        ar.name = ar.name[:30]
    ar.content = s
    return ar


def set_book_with_articles(a: List[str], book: Book):
    """
    a表示若干篇文章，把这些文章放到book里面
    :param a:
    :param book:
    :return:
    """
    p = Part()
    p.articles = [get_article(i) for i in a]
    book.parts = [p]


def show_books(books):
    """
    打印书籍列表及注释
    :param books:
    :return:
    """
    for book in books:
        print(book.name)
        for part in book.parts:
            for art in part.articles:
                print(art.name)
        print('========')


def split_by_pos(content: str, splitters: List[int]) -> List[str]:
    """
    对content按照splitter进行切分，切分成若干部分，每一部分都是一篇文章

    :param content:
    :param splitters:
    :return:
    """
    splitters = sorted(splitters)
    if len(splitters) and splitters[0] != 0:
        splitters.insert(0, 0)
    if len(splitters) and splitters[-1] != len(content):
        splitters.append(len(content))
    a = []
    for i in range(0, len(splitters) - 1):
        a.append(content[splitters[i]:splitters[i + 1]])
    return a


def get_pos(res: Iterable[re.Match]):
    """
    把res映射成int列表

    :param res:
    :return:
    """
    beg_list = []
    for i in res:
        beg = i.start()
        beg_list.append(beg)
    return beg_list
