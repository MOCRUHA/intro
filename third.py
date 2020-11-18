#3. Imprima o nome de todos os livros em ordem decrescente do número de páginas

import requests
from client import BooksApiClient


def get_pages(book):
    return book['pages']



def dec_pages_order():
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()

    sort_pages = sorted(books, key=get_pages, reverse=True)
    
    ordered_titles = [pages['title'] for pages in sort_pages]

    print(f"Titles in decrescet order of pages:\n\t{ordered_titles}")

    


dec_pages_order()