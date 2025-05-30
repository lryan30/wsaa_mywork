# flask server that links to a DAO
# author: LR

from flask import Flask, request, jsonify, abort
from bookDAO_skeleton import bookDAO

# This is a simple Flask application that provides a RESTful API for managing books.
# It uses a BookDAO class to interact with the data layer.
# The API supports the following operations:
# - GET /books: Get all books
# - GET /books/<id>: Get a book by ID
# - POST /books: Create a new book
# - PUT /books/<id>: Update a book by ID
# - DELETE /books/<id>: Delete a book by ID


app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# getall
# curl http://127.0.0.1:5000/books

@app.route('/books', methods=['GET'])
def getall():
        return jsonify(bookDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(bookDAO.findByID(id))

#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        book = {}

        if "title" not in jsonstring:
                abort(403)
        book["title"] = jsonstring["title"]
        if "author" not in jsonstring:
                abort(403)
        book["author"] = jsonstring["author"]
        if "price" not in jsonstring:
                abort(403)
        
        book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.create(book))

# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        book = {}

        if "title" in jsonstring:
                book["title"] = jsonstring["title"]
        if "author" in jsonstring:
                book["author"] = jsonstring["author"]
        if "price" in jsonstring:
                book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.update(id, book))

# Delete
# curl -X DELETE  http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(bookDAO.delete(id))


if __name__ == "__main__":
    app.run(debug = True)