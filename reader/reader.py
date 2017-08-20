from flask import Flask, request, send_file
import os
import json

app = Flask(__name__)

path = os.path.realpath(r'C:\Users\weidiao\Desktop\reader\电子书')


@app.route('/booklist')
def booklist():
    original_file = request.args['file'] if 'file' in request.args else ''
    file = os.path.join(path, original_file)
    if not os.path.exists(file):
        res = []
        print(file)
    if not file.startswith(path): return "baga ! "
    if os.path.isdir(file):
        res = []
        for i in os.listdir(file):
            if os.path.isdir(os.path.join(file, i)):
                res.append({'filename': i, 'isfolder': True, 'filepath': os.path.join(original_file, i)})
            else:
                res.append({'filename': i, 'isfolder': False, 'filepath': os.path.join(original_file, i)})
    res = json.dumps(res, ensure_ascii=0, indent=2)
    print(res)
    return res


@app.route('/book')
def book():
    book = request.args['book']
    pos = int(request.args['pos']) if 'pos' in request.args else 0
    pos = max(0, pos)
    sz = 1000
    filepath = os.path.join(path, book)
    if not filepath.startswith(path): return 'baga'
    with open(os.path.join(path, book), encoding='utf8') as f:
        content = f.read()
        res = content[pos:pos + sz]
    if not res:
        res = 'THE END'
    return res


if __name__ == '__main__':
    app.debug = True
    app.run()
