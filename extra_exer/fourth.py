#Qual é a média de páginas dentre todos os livros?

import requests

def pages_mean():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    t = 0
    for i in l:
        t = t + i['pages']
    avg = t / len(l)
    print(f"The average number of pages is: {avg}")
    

pages_mean()