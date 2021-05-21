import requests

book_request = requests.get("https://www.googleapis.com/books/v1/volumes", params=payload, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
print(book_request)