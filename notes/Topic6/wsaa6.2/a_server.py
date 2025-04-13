# simple flask web server script


from flask import Flask

app = Flask(__name__)  # can change name

@app.route('/')
def index():
    return "Hello Mamm\zdf\sdfy"

@app.route('/blah')
def blah():
    return "This is blah!"


if __name__ == '__main__':    # run script directly. it tells python to start the server if this script is run directly
    app.run(debug=True)            # app.run() will start the Flask development server.

# To run the server, use the command: python a_server.py