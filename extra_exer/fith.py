#5. Qual é o desvio padrão do número de páginas dentre todos os livros?

import requests
from statistics import pstdev 

def std_dev_pages():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    #create list with number of pages
    pages = []
    for i in l:
        pages.append(i['pages'])
    #std dev call
    st = pstdev(pages)
    print(f"The standard deviation for the number of pages is; {st}")

std_dev_pages()