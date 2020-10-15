'''9. Ordene todos os livros por quantidade de página ascendentemente 
    e imprima apenas os livros cuja posição na lista é divisível por 3 ou por 5'''

import requests

def asc_pages_order():

    #do resquests

    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    sort_pages = sorted(l, key=lambda i: i['pages'])

    #create and sort list

    ordered_titles = []
    for t in sort_pages:
        ordered_titles.append(t['title'])
    print(ordered_titles)
    #select divisible for 3 or 5

    for title in range(len(ordered_titles)):
        if (title % 3 == 0 or title % 5 == 0) and (title != 0):
            print(ordered_titles[title], title)
            

asc_pages_order()