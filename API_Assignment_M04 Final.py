# API Assignment for SDEV 220
# Author: Kyrylo Mizernyuk
# Date: November 20, 2023
# Description: This program implements a RESTful API for managing a collection of books. 
# It provides endpoints for creating, reading, updating, and deleting book entries.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize an empty list to store books. Each book is a dictionary.
books = []

@app.route('/books', methods=['GET'])
def get_books():
    """
    Retrieve and return the list of all books.
    """
    return jsonify(books)

@app.route('/books', methods=['POST'])
def create_book():
    """
    Create a new book entry from the provided JSON data and add it to the books list.
    """
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Retrieve and return a book by its ID.
    """
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update an existing book's information with the provided JSON data.
    """
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        updated_book = request.get_json()
        book.update(updated_book)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Delete a book by its ID from the books list.
    """
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 204

if __name__ == '__main__':
    # Run the Flask app with debug mode on to enable auto-reloading on code changes.
    app.run(debug=True)
