# book_api.py-->functions to get, add, update and delete books from the api, stored here, not called just defined, will be called in test.py
# test.py is the main script where the functions are called. eg: calculate avg price of books


import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
#print(response.status_code) 
# print(response.text) 
# print(response.json())

def get_books():
    try:
       response = requests.get(URL)
       response.raise_for_status()
       return response.json()
        
    except requests.RequestException as e:
        print(f"Error: {e}")
      # return []

def readbooks():
    response = requests.get(URL)
    return response.json()

if __name__ == "__main__":

 print(readbooks())


def readbook(id):
    geturl = URL + '/' + str(id)
    response = requests.get(geturl)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    else:
        return response.json()

print(readbook(1118))    

import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def createbook(book):
    headers = {'Content-Type': 'application/json'}
    
    # Send a POST request to create a new book
    response = requests.post(URL, json=book, headers=headers)

    # Check the status code:
    if response.status_code == 201:
        print("Book created successfully!")
        return response.json()
    elif response.status_code == 200:
        print("Received status 200 OK, but creation may not have happened.")
        print(f"Response content: {response.text}")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

# Create a new book
if __name__ == "__main__":     # test if this script is run directly 
    # Example book data to create
    new_book = {
        "title": "New Book",
        "author": "John Doe",
        "price": 19.99
    }
    created_book = createbook(new_book)

    if created_book:
        print("Created Book:", created_book)
    else:
        print("Failed to create book.")

# update books using put method:

def update_book(book_id, book):
    updateurl = URL + '/' + str(book_id)
    response = requests.put(updateurl, json=book)
    
    if response.status_code == 200:
        print("Book updated successfully!")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None