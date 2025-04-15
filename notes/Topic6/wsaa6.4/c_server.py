
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/inquery', methods=['GET'])
def inquery():
    # Get the query parameter 'name' from the URL.
    name = request.args['name']
    return request.args  # Return the entire query string as a response. for designing api and want to use arguments in the URL.
# return name  # Return the name parameter as a response.

# can also pass json object it in body of post request (postman)
@app.route('/inbody', methods=['POST'])
def inbody():
    name = request.json['name']
    age = request.json['age']
   # print(request.json)  # Print the entire JSON object received in the request body.
    return f'you are {name} and age is {age}'  # Return the name and age as a response.

# dict object to be returned as json object
@app.route('/user')
def getuser():
    user={
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(user)  # Return the user dictionary as a JSON response.




if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask development server with debug mode enabled.