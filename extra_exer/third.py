#3. Imprima o nome de todos os livros em ordem decrescente do número de páginas

import requests

def dec_pages_order():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    sort_pages = sorted(l, key=lambda i: i['pages'], reverse=True)
    ordered_titles = []
    for t in sort_pages:
        ordered_titles.append(t['title'])
    print(f"Titles in decrescet order of pages:\n\t{ordered_titles}")

dec_pages_order()