import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('warm-up-project-3050-38ab8-c4e39881987b.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()