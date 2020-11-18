#add a book

import requests

def add_a_book():
    isbn = input("Type isbn for the book:\n")
    title = input("Type the title of the book:\n")
    pages = input("Type how many pages the book has:\n")
    r = requests.post("http://0.0.0.0:8000/books", data ={"isbn":isbn, "title":title, "pages":pages})
    r = requests.get("http://0.0.0.0:8000/books")
    print(r.text)

add_a_book()