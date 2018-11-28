import requests
import time
import pyrebase
from tqdm import tqdm

config={"apiKey": "AIzaSyChJD9SNw8rQlFw_eVUlgpuaiUfChl9xok",
        "authDomain":"148555283319.firebaseapp.com",
        "databaseURL":"https://musictube-75f00.firebaseio.com",
        "storageBucket":"musictube-75f00.appspot.com"
}
t=[]
d=[]
timestamp=int(time.time())

with open('youtube_code_punjabi.txt','r') as f:
    lines_f1=f.read().splitlines()

with open('youtube_title_punjabi.txt','r') as f:
    lines_f2=f.read().splitlines()

for line in lines_f1:
    t.append(line)

for line in lines_f2:
    d.append(line)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
for i in tqdm(range(len(t))):
    data={'t':t[i],'d':d[i],'s':timestamp}
    result = db.child("Punjabi").push(data)
    print(result)
