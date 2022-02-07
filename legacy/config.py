import os
from os import path

ebook = path.join(path.dirname(__file__), '../ebook')
db_path = path.join(path.dirname(__file__), '../book.db')
index_path = path.join(path.dirname(__file__), '../index.json')
if __name__ == '__main__':
    print(os.listdir(ebook))
