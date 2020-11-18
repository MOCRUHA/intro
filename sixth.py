#6. Qual é o quinto livro com o menor número de páginas?

import requests
from client import BooksApiClient


def fith_least_pages():
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()

    sort_pages = sorted(books, key=lambda book: book['pages'])
    
    ordered_titles = [book['title'] for book in sort_pages]
   
    print(f"The fith book with less pages is:\n\t{ordered_titles[4]}")

fith_least_pages()



