import requests
import time
from bs4 import BeautifulSoup
from firebase import firebase

timestamp=int(time.time())

with open('youtube_code.txt') as f:
    youtube_code_previous=f.read().splitlines()[0]


url='https://imvdb.com/new/'
header={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response= requests.get(url,header,timeout=10)
soup=BeautifulSoup(response.content,'html.parser')
songs_list=soup.find_all('div',class_='rack_node')
songs_link=[]
d=[]
t=[]
counter=0
if response.status_code!=200:
    print(response.status_code)
else:
    for i in songs_list:
        counter+=1
        print('hi i am in first for loop '+str(counter))
        link=i.findNext('a')
        views=i.findNext('span',class_='views')
        if int(views['data-views']) >=300000:
            songs_link.append(link['href'])

    counter=0
    print(len(songs_link))

    for link in songs_link:
        try:
            response=requests.get(link,header,timeout=60)
        except requests.exceptions.RequestException as e:
            print (e)
            continue

        if response.status_code!=200:
            print(response.status_code)
        else:
            counter+=1
            print('hi i am in second for loop '+str(counter))
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

            time.sleep(5)

if len(d)>0:
    with open('youtube_code.txt','w') as f:
        for item in t:
            f.write("%s\n" % item)

    with open('youtube_title.txt','w') as f:
        for item in d:
            f.write("%s\n" % item)
