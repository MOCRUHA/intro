#count books

import requests

def count_books():
    l = requests.get("http://0.0.0.0:8000/books")
    c = l.text
    total = str(c.count("isbn"))
    print("We have " + total + " books registered.")
    
count_books()