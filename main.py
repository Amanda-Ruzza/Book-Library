from flask import Flask, request, Response
import json

app = Flask(__name__)

# KEY : VALUE
books_db = {
    "1": {"name": "Crime and Punishment", "release_date": "1886"},
    "2": {"name": "XX", "release_date": "1111"},     #write the book name and release date for every book
    "3": {"name": "abc", "release_date": "1112"}
}

# I don't need to define the GET METHOD using Flask, however, it's mandatory that I define the POST, PUT or DELETE methods
@app.route("/hello") #we're going to tell the application to create a root and the root is going to execute the function "/hello" and it will return the function
def hello():
    return "Good Morning"

@app.route("/books") # This is the route for the Book Library Database
def book_list():
    return books_db

@app.route("/books_rating", methods=['PUT']) #Trying to update my book list dictionary by adding a master rating to the list
def books_rating ():
    return "From 1 to 5, how would you rate this list?" 
    if request.methods == 'PUT' :
            "1"
            return books_db.append("This list has a 1 star rating")
    else :
            return books_db.append("This is a highly rated book list")

@app.route("/book/new_book", methods=['POST']) #trying to add a book to my book list
def add_book():
    # Collect the new book from the user/url
    request_data = request.get_json() # Use the 'request' function on python to REQUEST DATA from the user
   
    # Extract the movie data from the request
    new_book = request_data['book']
    # Get the last position in the database
    new_id = len(books_db) + 1
    # create a new new entry for my movie
    new_book_data = { str(new_id) : new_book }
    # Update 
    books_db.update(new_book_data)
    return "This book was added successfully"


 # Using the POST METHOD to update an element in the list, for example the <release_date>. I can also use the PUT METHOD to do this   
@app.route("/book/update_book_information", methods=['POST'])
def update_book_info():
    request_data = request.get_json()
    books_db.update(request_data)
    return "This book was updated"

@app.route("/books/delete_books/<book_id>")
def delete_books(book_id):
    del books_db[book_id]
    return "This book was removed"
   
    
@app.route("/book/<book_id>") #This is a GET METHOD. The GET Method is just to collect something
def get_book(book_id):
    return books_db[book_id]


if __name__ == "__main__":
    app.run(host="127.0.0.1") # The Host will be the IP address of my own machine
