#Qual é a média de páginas dentre todos os livros?

import requests
from client import BooksApiClient

def pages_mean():
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()

    avg = sum([book['pages'] for book in books]) / len(books)
    
    print(f"The average number of pages is: {avg:.2f}")
    
    

pages_mean()