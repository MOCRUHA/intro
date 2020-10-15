#6. Qual é o quinto livro com o menor número de páginas?


import requests

def fith_least_pages():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    sort_pages = sorted(l, key=lambda i: i['pages'], reverse=True)
    ordered_titles = []
    for t in sort_pages:
        ordered_titles.append(t['title'])
    print(f"The fith book with less pages is:\n\t{ordered_titles[-5]}")

fith_least_pages()