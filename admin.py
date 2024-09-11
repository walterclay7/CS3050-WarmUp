# Read json info into python

import json

with open('books.json', 'r') as file:
    books = json.load(file)

print(books)