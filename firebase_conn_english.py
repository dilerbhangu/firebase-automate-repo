import pyrebase
import passwords
import time
from tqdm import tqdm

config={"apiKey": passwords.API_KEY,
        "authDomain":passwords.AUTH_DOMAIN,
        "databaseURL":passwords.DATABASE_URL,
        "storageBucket":passwords.STROAGE_BUCKET
}
timestamp=int(time.time())

with open('youtube_code_english.txt','r') as f:
    lines_f1=f.read().splitlines()

with open('youtube_title_english.txt','r') as f:
    lines_f2=f.read().splitlines()

t=[]
d=[]

for line in lines_f1:
    t.append(line)

for line in lines_f2:
    d.append(line)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

with open('result.txt') as res_file:
for i in tqdm(range(len(t))):
    for j in range(10):
        try:
            data={'t':t[i],'d':d[i],'s':timestamp}
            result = db.child("English").push(data)
        except Exception as e:
            time.sleep(5)
            print(e)
        else:
            break
