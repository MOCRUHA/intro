#add several random books
import requests
import random
import string

def add_a_book2():
    for b in range(50):
        isbn = random.randint(1000, 1000000)
        title = ''.join(random.choices(string.ascii_lowercase+string.digits, k=8))
        pages = random.randint(200, 999) 
        r = requests.post("http://0.0.0.0:8000/books", data ={"isbn":isbn, "title":title, "pages":pages})
    print(r.text)

add_a_book2()