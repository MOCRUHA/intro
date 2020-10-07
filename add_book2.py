#add a book2

import requests

def add_a_book2(isbn, title, pages):
    r = requests.post("http://0.0.0.0:8000/books", data ={"isbn":isbn, "title":title, "pages":pages})
    print(r.text)

add_a_book2()