
# static_url_path is the URL path for static files, static_folder is the folder name for static files
# This allows you to serve static files (like HTML, CSS, JS) from a specific folder in your project
# without needing to specify the folder name in the URL.

from flask import Flask
from flask import redirect, url_for


app = Flask(__name__, static_url_path='', static_folder='staticpages')

# mapping
@app.route('/')                    #'/' # root URL 
def index():
    return '<h1>Hi There L!</h1>'

@app.route('/users', methods=['GET'])    # get all users
def get_users():
    return 'Getting all users!'

@app.route('/users/<username>', methods=['GET'])    # get user by username
def get_user_byname(username):              # <username> is a variable part of the URL 
    return f'Hello {username}'             # {} brackets are used to insert the value of the variable into the string   


@app.route('/users/by-id/<int:id>', methods=['GET'])    # get user by id
def get_user_byid(id):
    return f'Your id is {id}'


@app.route('/users', methods=['POST'])  # create a new user
def create_user():
    return 'Creating user!'


@app.route('/users', methods=['PUT'])    # update a user
def update_users():
    return 'Update user!'

@app.route('/invalid', methods=['GET'])    # invalid URL
def testingredirect():
    return redirect(url_for('index'))    # redirect to the index page

@app.route('/square/<int:id>', methods=['GET'])    # get square of a number
def get_square(id):
    return f'The square of {id} is {id**2}'

if __name__ == '__main__':           # run script directly. it tells python to start the server if this script is run directly
    app.run(debug=False)