import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import passwords
import pyrebase

def English():
    config={"apiKey": passwords.API_KEY,
            "authDomain":passwords.AUTH_DOMAIN,
            "databaseURL":passwords.DATABASE_URL,
            "storageBucket":passwords.STROAGE_BUCKET
    }
    timestamp=int(time.time())

    with open('youtube_code_english.txt') as f:
        youtube_code_previous=f.read().splitlines()[0]


    url='https://imvdb.com/new/'
    header={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response= requests.get(url,header,timeout=10)
    soup=BeautifulSoup(response.content,'html.parser')
    songs_list=soup.find_all('div',class_='rack_node')
    songs_link=[]
    d=[]
    t=[]

    if response.status_code!=200:
        print(response.status_code)
    else:
        for i in tqdm(songs_list):
            link=i.findNext('a')
            views=i.findNext('span',class_='views')
            if int(views['data-views']) >=300000:
                songs_link.append(link['href'])

        print(len(songs_link))

        for link in tqdm(songs_link):
            for i in range(10):
                try:
                    response=requests.get(link,timeout=30)
                except requests.exceptions.RequestException as e:
                    print(e)
                    time.sleep(5)
                else:
                    response=response
                    break

            if response.status_code==200:
                soup=BeautifulSoup(response.content,'html.parser')
                video_title=soup.find('div',id='videoTitle')
                video_info=soup.find_all('ul',class_='videoInfoList')
                s1=video_title.findNext('h1').text
                s1=s1.split(' \t',1)[0]

                s2=video_info[-1].findNext('a')
                s2=s2['href']
                s2=s2.split('https://www.youtube.com/watch?v=',1)[1]

                if s2==youtube_code_previous:
                    break

                t.append(s2)
                d.append(s1)


    if len(d)>0:
        with open('youtube_code_english.txt','w') as f:
            for item in t:
                f.write("%s\n" % item)

        with open('youtube_title_english.txt','w') as f:
            for item in d:
                f.write("%s\n" % item)

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
        for i in tqdm(range(len(t))):
            for j in range(10):
                try:
                    data={'t':t[i],'d':d[i],'s':timestamp}
                    result = db.child("English").push(data)
                except requests.exceptions.RequestException as e:
                    print(e)
                else:
                    break
