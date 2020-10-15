
import requests

def delete():
    url = "http://0.0.0.0:8000/books"
    r = requests.get(f"{url}")
    books = r.json()
    for book in books:
        requests.delete(f"{url}/{book['isbn']}")
    print("All items deleted!")

delete()