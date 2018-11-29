import requests
import time
import pyrebase
import passwords
from tqdm import tqdm

config={"apiKey": passwords.API_KEY,
        "authDomain":passwords.AUTH_DOMAIN,
        "databaseURL":passwords.DATABASE_URL,
        "storageBucket":passwords.STROAGE_BUCKET
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
    for i in range(10):
        try:
            data={'t':t[i],'d':d[i],'s':timestamp}
            result = db.child("Punjabi").push(data)
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            break
