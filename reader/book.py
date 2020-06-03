from typing import List
from fu.dict_obj import DictObj


class Article(DictObj):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.content = ''  # 这是最终的内容


class Part(DictObj):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.articles: List[Article] = []  # 一个部分是由若干个课文组成的


class Book(DictObj):
    def __init__(self):
        super().__init__()
        self.name = 'book'
        self.author = 'author'
        self.tags: List[str] = []  # 书籍的标签
        self.parts: List[Part] = []  # 书籍的部分


def get_article(s: str):
    ar = Article()
    ar.name = s.strip().splitlines()[0]  # 以第一行为题目
    ar.content = s
    return ar


def set_book_with_articles(a: List[str], book: Book):
    p = Part()
    p.articles = [get_article(i) for i in a]
    book.parts = [p]


def show_books(books):
    for book in books:
        print(book.name)
        for part in book.parts:
            for art in part.articles:
                print(art.name)
        print('========')
