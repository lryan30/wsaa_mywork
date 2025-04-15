# This is a simple REST server using Flask
# books


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')     # Route for the root URL/homepage
def index():        # This function will be called when the root URL is accessed 
    return "Hello, World!"


@app.route('/books', methods=['GET'])  # Route for the /books URL
def getall():
    return "Get all books!"


@app.route('/books/<int:id>', methods=['GET'])  # Route for the /books URL
def findbyid(id):  # This function will be called when the /books/<id> URL is accessed
    return "get id {id}!"


@app.route('/books', methods=['POST'])  
def create():
    jsonstring = request.json
    return f"Create a new book!{jsonstring}"


@app.route('/books/<int:id>', methods=['PUT'])
def update(id):  
    jsonstring = request.json  # read json from the body
    return f"Update book with id {id}{jsonstring}"


@app.route('/books/<int:id>', methods=['DELETE'])  
def delete(id):
    return f"Delete {id}!"


if __name__ == '__main__':  
    app.run(debug=True)  