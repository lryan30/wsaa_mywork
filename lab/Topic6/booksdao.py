
from flask import Flask, jsonify, request, abort, for_url
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# returns all the books in the database table:
def getall():
    return [{}]

# returns one book:
def findbyid(id):
    return {}


# inserts a book into the database:
def create(book):
    book.append(book)
    return book
   

# updates a book:
def update(id, book):
    return book

# deletes a book:
def delete(id):
    return True




if __name__ == "__main__":
    app.run(debug=True)