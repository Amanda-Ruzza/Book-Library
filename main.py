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

@app.route("/books_rating", methods = ['PUT']) #Trying to update my book list dictionary by adding a master rating to the list
def books_rating ():
    return "From 1 to 5, how would you rate this list?" 
    if request.methods == 'PUT' :
            "1"
            return books_db.append("This list has a 1 star rating")
    else :
            return books_db.append("This is a highly rated book list")

@app.route("/new_book", methods = ['POST']) #trying to add a book to my book list
def new_book_request():
    return "Would you like to add your favorite book to this list? Type yes or no "
    if request :
        "yes"
        def new_book():
            {"4": {"name": "abc", "release_date": "1112"}}
            books_db.append(new_book)


if __name__ == "__main__":
    app.run(host="127.0.1") # The Host will be the IP address of my own machine
