#2. Imprima o nome de todos os livros em ordem alfabética

import requests
from client import BooksApiClient

def sort_name():
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()
    
    sorted_names = sorted([book['title'] for book in books])
  
    print(sorted_names)

sort_name()