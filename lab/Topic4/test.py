# test.py used to import and call the functions defined in book_api.py


from book_api import get_books

def calculate_average_price():
    books = get_books()
    if not books:
        print("No books found or error in fetching data.")
        return

    total_price = 0
    count = 0
    for book in books:
        if "price" in book and isinstance(book["price"], (int, float)):
            total_price += book["price"]
            count += 1

    if count == 0:
        print("No price data available.")
    else:
        average = total_price / count
        print(f"Average book price: €{average:.2f}")


if __name__ == "__main__":   
    calculate_average_price()



from book_api import update_book

# Use the correct ID of the created book
book_id = 1118

# Include all required fields (id)
updated_book_data = {
    "title": "Updated Title from test.py",
    "author": "Updated Author",
    "price": 42.99
}

# Call the function and store the response
updated = update_book(book_id, updated_book_data)

# Print the actual response from the server
if updated:
    print("Updated Book:", updated)
else:
    print("Failed to update book.")
