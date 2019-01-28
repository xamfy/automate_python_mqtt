import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate(
    'serviceAccountKey.json')
firebase_admin = firebase_admin.initialize_app(
    cred, {'databaseURL': 'YOUR_DB_URL'})


def listener(event):
    # print(event.event_type)
    # print(event.path)
    print(event.data)
    # if(len(event.data) == 2):
    # print(event.data['name'] + " " + str(event.data['status']))
    # print(event.data)


db.reference('/devices').listen(listener)
