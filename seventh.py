#Imprima o isbn de todos os livros que têm um número ímpar de caracteres no titulo.

import requests
from client import BooksApiClient


def odd_title_char():
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()
    
    print("The following isbn have odd number of characteres: ")

    odds = [
        book['isbn'] for book in books if len(book['title']) % 2 != 0
    ]
    
    print(odds)

odd_title_char()