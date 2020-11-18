import requests


class BooksApiClient:

    def __init__(self, url):
        self.base_url = url

    def create_book(self, isbn, title, pages):
        r = requests.post(
            self.base_url,
            data ={"isbn":isbn, "title":title, "pages":pages}
        )
        return r.content               
    
    def list_books(self):
        r = requests.get(
            self.base_url
        )
        return r.json()    

    def book_details(self, isbn):
        r = requests.get(
            f"{self.base_url}/{isbn}"
        )
        return r.json()        
    
    def delete_book(self, isbn):
        r = requests.delete(
            f"{self.base_url}/{isbn}"
        )
        



