#1. Qual é o livro com o maior número de páginas? (retorne o dicionário inteiro)

import requests

def max_page_number():
    r = requests.get("http://0.0.0.0:8000/books")
    books = r.json()
    max_pages = 0
    for book in books:
        if max_pages < i['pages']:
            max_pages = i['pages']
            dic = book
    print(dic)

           
max_page_number()