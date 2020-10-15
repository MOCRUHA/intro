#2. Imprima o nome de todos os livros em ordem alfabética

import requests

def sort_name():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    names = []
    for i in l:
        names.append(i['title'])
    f = sorted(names)
    print(f)


sort_name()