from config_firestore import db
import firebase_admin
from google.cloud.firestore_v1 import FieldFilter

def query_retrieve(keyword, operator, user_ln):
    pass
    # Check for 1 or 2 queries (maybe recursion)

    # Hard code 4 cases

    # Single queries

    # Compund queries

    # The ALL

    # Return list of all books




docs = (db.collection('books')
        .where(filter=FieldFilter('author', '==', 'J.R.R. Tolkien'))
        )

docs2 = (docs.where(filter=FieldFilter('published_year', '<', 1940))
         .stream())
# Set of (remove duplicates)
for doc in docs2:
    print(doc.to_dict())