import requests
import time
import pyrebase

config={"apiKey": "AIzaSyChJD9SNw8rQlFw_eVUlgpuaiUfChl9xok",
        "authDomain":"148555283319.firebaseapp.com",
        "databaseURL":"https://musictube-75f00.firebaseio.com",
        "storageBucket":"musictube-75f00.appspot.com"
}
t=[]
d=[]
timestamp=int(time.time())

with open('youtube_code.txt','r') as f:
    lines_f1=f1.read().splitlines()

with open('youtube_title.txt','r') as f:
    lines_f2=f2.read().splitlines()

for line in lines_f1:
    t.append(line)

for line in lines_f2:
    d.append(line)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
for i in range(len(t)):
    data={'t':t[i],'d':d[i],'s':timestamp}
    result = db.child("English").push(data)
    print(result)
