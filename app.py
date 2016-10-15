from flask import Flask
from flask import jsonify, make_response
from flask import request

app = Flask('Jay-library')

books = [{
        'name': 'Harry Potter and the prisoner of Azkaban',
        'author': 'JK. Rowling',
        'category': 'magic/Fiction',
        'id':'1243'
         }
       ]
@app.route('/api/category/books/', methods=('GET','POST'))
def book_api():
    resp = ''
    if request.method == 'GET':
        return make_response(jsonify(books))
        resp = jsonify(books)
    else:
        name = request.values.get('name', None)
        author =request.values.get('author', None)
        category =request.values.get('category', None)
        id_ =request.values.get('id', None)

        new_book = {
                'name': name,
                'author': author,
                'category': category,
                'id': id_
                }
        books.append(new_book)
        return jsonify({'OK':'Book added'})

    return resp

if __name__=='__main__':
    app.run()
