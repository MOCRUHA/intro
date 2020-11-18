'''9. Ordene todos os livros por quantidade de página ascendentemente 
    e imprima apenas os livros cuja posição na lista é divisível por 3 ou por 5'''

import requests
from client import BooksApiClient


def asc_pages_order():

    #do resquests
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()
    
    sort_pages = sorted(books, key=lambda book: book['pages'])

    #create and sort list
    ordered_titles = [item['title'] for item in sort_pages]
    
    #for t in sort_pages:
    #    ordered_titles.append(t['title'])
    #print(ordered_titles)

    #select divisible for 3 or 5
    for title in range(len(ordered_titles)):
        if (title % 3 == 0 or title % 5 == 0) and (title != 0):
            print(ordered_titles[title], title)
            

asc_pages_order()