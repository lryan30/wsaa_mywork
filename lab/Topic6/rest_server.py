# Lab Topic 6: Rest API 

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# index:
@app.route('/')
def index():
    return "hello"

# books:
@app.route('/books', methods = ['GET'])
def findby():
    return "find books"

# find by id:
@app.route('/books/<int:id>', methods = ['GET'])
def findbyid(id):
    return f"find book {id}"

# create:
@app.route('/books', methods = ['POST'])
def create():
    data= request.get_json()
    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    return f"created book: {title}, {author}, {price}"

# update:
@app.route('/books/<int:id>', methods = ['PUT'])
def update(id):
    return f"update book {id}"

# delete:
@app.route('/books/<int:id>', methods = ['DELETE'])
def delete(id):
    return f"delete {id}"



if __name__ == "__main__":
    app.run(debug=True)



