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
                book = doc.to_dict()
                if key in book:
                    result.append(book[key])
            #remove duplicates
            result = set(result)
        else:
            docs = db.collection('books').where(filter=FieldFilter(key,op,line)).stream()
            if(key == 'title'):
                for doc in docs:
                    for vals in doc.to_dict().values(): 
                        result.append(vals)
            else:
                for doc in docs:
                    result.append(doc.to_dict()['title'])

    # Compund queries
    else:
        # First query
        line1 = user_ln[0]
        op1 = operator[0]
        key1 = keyword[0]

        # Second query
        line2 = user_ln[1]
        op2 = operator[1]
        key2 = keyword[1]

        docs = (db.collection('books')
            .where(filter=FieldFilter(line1, op1, key1))
            .where(filter=FieldFilter(line2, op2, key2))
            .stream())



    return result




# # Set of (remove duplicates)
# for doc in docs:
#    print(doc.to_dict()['title'])