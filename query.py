from config_firestore import db
import firebase_admin
from google.cloud.firestore_v1 import FieldFilter

def query_retrieve(keyword, operator, user_ln):
    # Check for 1 or 2 queries 
    result = []

    if len(keyword) == 1:
        line = user_ln[0]
        op = operator[0]
        key = keyword[0]
        if(line == 'ALL'):
            #get all books
            docs = db.collection('books').stream()

            #for each book, get the info they are looking for
            for doc in docs:
                result.append(doc.to_dict()[key])
            #remove duplicates
            result = set(result)
        else:
            print(key)
            print(op)
            print(line)
            docs = db.collection('books').where(filter=FieldFilter(key,op,line)).stream()
            if(key == 'title'):
                for doc in docs:
                    result.append(doc.to_dict().values())
            else:
                for doc in docs:
                    result.append(doc.to_dict()['title'])

    # Compund queries
    else:
        pass

    return result
    




docs = (db.collection('books')
        .where(filter=FieldFilter('author', '==', 'J.R.R. Tolkien'))
        .where(filter=FieldFilter('published_year', '<', 1940))
        .stream())

# Set of (remove duplicates)
for doc in docs:
    print(doc.to_dict()['title'])