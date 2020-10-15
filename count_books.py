#count books

import requests

def count_books():
    r = requests.get("http://0.0.0.0:8000/books")
    total = len(r.json())
    print(f"We have {total} books registered.")
    
count_books() 