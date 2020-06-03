from reader.adapters import 金庸, 毛泽东, 东野圭吾,章回体小说

books = []
books.extend(金庸.books)
books.extend(毛泽东.books)
books.extend(东野圭吾.books)
books.extend(章回体小说.books)
if __name__ == '__main__':
    print(len(books))
