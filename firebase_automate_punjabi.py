import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

with open('youtube_code_punjabi.txt') as f:
    youtube_code_previous=f.read().splitlines()[0]

url='https://www.mrhd.in/punjabi/'
try:
    response=requests.get(url,timeout=10)
except requests.exceptions.RequestException as e:
    print(e)
else:
    soup=BeautifulSoup(response.content,'html.parser')
    songs_list=soup.find_all('div',class_='mh-loop-thumb')

    songs_links=[]
    d=[]
    t=[]

    for song in tqdm(songs_list):
        songs_links.append(song.findNext('a')['href'])

    for link in tqdm(songs_links):
        for i in range(10):
            try:
                response=requests.get(link,timeout=30)
            except requests.exceptions.RequestException as e:
                print(e)
                time.sleep(5)
            else:
                break

        soup=BeautifulSoup(response.content,'html.parser')
        video_info=soup.find('iframe')['src']
        video_info=video_info.split('//www.youtube.com/embed/',1)[1]

        video_title=soup.find('h1',class_='entry-title').get_text()
        video_title=video_title.split(' Video HD  Download',1)

        if video_info==youtube_code_previous:
            break
        t.append(video_info)
        d.append(video_title[0])


if len(d)>0:
    with open('youtube_code_punjabi.txt','w') as f:
        for item in t:
            f.write('%s\n'%item)

    with open('youtube_title_punjabi.txt','w') as f:
        for item in d:
            f.write('%s\n'%item)
