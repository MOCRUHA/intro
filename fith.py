#5. Qual é o desvio padrão do número de páginas dentre todos os livros?

import requests
from client import BooksApiClient
from statistics import pstdev 

def std_dev_pages():
    client = BooksApiClient("http://0.0.0.0:8000/books")
    books = client.list_books()
    
    #create list with number of pages
    pages = [item['pages'] for item in books ]
    
    #std dev call
    st = pstdev(pages)
    print(f"The standard deviation for the number of pages is; {st}")

std_dev_pages()