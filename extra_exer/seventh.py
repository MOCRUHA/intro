#Imprima o isbn de todos os livros que têm um número ímpar de caracteres no titulo.

import requests

def odd_title_char():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()
    print("The following isbn have odd number of characteres: ")
    for i in l:
        t = len(i['title'])
        x = i
        if t % 2 != 0:
            print(i['isbn'])
odd_title_char()