from config_firestore import db
import json

with open('books.json', 'r') as file:
    books = json.load(file)

print(books)