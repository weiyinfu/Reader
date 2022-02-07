import importlib
import os
import sys
from os.path import *

"""
adapters中文件的封装
"""
adapters = join(dirname(__file__), 'adapters')
sys.path.insert(0, adapters)
books = []
for i in os.listdir(adapters):
    if i.startswith('__'): continue
    mod = importlib.import_module(i[:i.rindex('.')])
    books.extend(mod.books)
if __name__ == '__main__':
    print(len(books))
