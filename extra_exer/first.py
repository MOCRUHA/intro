#1. Qual é o livro com o maior número de páginas? (retorne o dicionário inteiro)

import requests

def max_page_number():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    m = 0
    for i in l:
        if m < i['pages']:
            m = i['pages']
            x = i
    print(x)

           
max_page_number()