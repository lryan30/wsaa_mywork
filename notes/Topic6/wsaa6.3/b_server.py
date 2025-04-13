from flask import Flask

# static_url_path is the URL path for static files, static_folder is the folder name for static files
# This allows you to serve static files (like HTML, CSS, JS) from a specific folder in your project
# without needing to specify the folder name in the URL.

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# mapping


if __name__ == '__main__': 
    app.run(debug=True)