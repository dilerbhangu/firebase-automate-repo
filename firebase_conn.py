import requests
import time
from firebase import firebase
import pyrebase
config={"apiKey": "AIzaSyChJD9SNw8rQlFw_eVUlgpuaiUfChl9xok",
        "authDomain":"148555283319.firebaseapp.com",
        "databaseURL":"https://musictube-75f00.firebaseio.com",
        "storageBucket":"musictube-75f00.appspot.com"
}

timestamp=int(time.time())
file1 = open("youtube_code.txt","r")
file2 = open("descripition.txt","r")
t=[]
d=[]
for word in file1.read().split():
    t.append(word)

for word in file2.read().split():
    d.append(word)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
for i in range(len(t)):
    data={'t':t[i],'d':d[i],'s':timestamp}
    result = db.child("English").push(data)
    print(result)
