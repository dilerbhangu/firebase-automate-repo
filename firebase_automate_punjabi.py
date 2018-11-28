import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

url='https://www.mrhd.in/punjabi/'
try:
    response=requests.get(url,timeout=10)
except requests.exceptions.RequestException as e:
    print(e)

if response.status_code==200:
    soup=BeautifulSoup(response.content,'html.parser')
    songs_list=soup.find_all('div',class_='mh-loop-thumb')

    songs_links=[]
    d=[]
    t=[]

    for song in tqdm(songs_list):
        songs_links.append(song.findNext('a')['href'])

    for link in tqdm(songs_links):
        try:
            response=requests.get(link,timeout=30)
        except requests.exceptions.RequestException as e:
            print(e)

        if response.status_code==200:
            soup=BeautifulSoup(response.content,'html.parser')
            video_info=soup.find('iframe')['src']
            video_info=video_info.split('//www.youtube.com/embed/',1)[1]
            t.append(video_info)

            video_title=soup.find('h1',class_='entry-title').get_text()
            video_title=video_title.split(' Video HD  Download',1)[0]
            d.append(video_title)


if len(d):
    with open('youtube_code_punjabi.txt','w') as f:
        for item in t:
            f.write('%s\n'%item)

    with open('youtube_title_punjabi.txt','w') as f:
        for item in d:
            f.write('%s\n'%item)
