from os import path
import os

char_count = 0
lines_count = 0
for parent, folders, files in os.walk('ebook'):
    if '.git' in parent:
        continue
    for file in files:
        filepath = path.join(parent, file)
        print(filepath)
        content = open(filepath).read()
        lines_count += content.splitlines().__len__()
        char_count += len(content)
print(char_count, lines_count)
