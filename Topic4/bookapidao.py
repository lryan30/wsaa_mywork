# module that provides a set of functions to interact with book api hosted at PythonAnywhere


import requests
import json

url = 'http://andrewbeatty1.pythonanywhere.com/api/books/'

def get_books():
    """Get all books from the API."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
    