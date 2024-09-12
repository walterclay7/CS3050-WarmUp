from config_firestore import db
import json

with open('books.json', 'r') as file:
    books = json.load(file)

for i, book in enumerate(books):
    doc_ref = db.collection("books").document(books[i]['title'])
    doc_ref.set(book)