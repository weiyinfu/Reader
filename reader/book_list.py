from reader.adapters import 金庸, 毛泽东, 东野圭吾, 章回体小说
import sys
import os
import importlib
from os.path import *

adapters = join(dirname(__file__), 'adapters')
sys.path.insert(0, adapters)
books = []
for i in os.listdir(adapters):
    if i.startswith('__'): continue
    mod = importlib.import_module(i[:i.rindex('.')])
    books.extend(mod.books)
if __name__ == '__main__':
    print(len(books))
