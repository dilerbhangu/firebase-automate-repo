import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import passwords
import pyrebase
import firebase_conn_hindi

config = {"apiKey": passwords.API_KEY,
          "authDomain": passwords.AUTH_DOMAIN,
          "databaseURL": passwords.DATABASE_URL,
          "storageBucket": passwords.STROAGE_BUCKET
          }
timestamp = int(time.time())

PATH='/home/bhangutech/Python Projects/firebase-automate-repo/'

with open(PATH+'youtube_code_hindi.txt') as f:
    youtube_code_previous = f.read().splitlines()[0]

url = 'https://www.mrhd.in/hindi/'
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    print(e)
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    songs_list = soup.find_all('div', class_='mh-loop-thumb')

    songs_links = []
    d = []
    t = []

    for song in tqdm(songs_list):
        songs_links.append(song.findNext('a')['href'])

    for link in tqdm(songs_links):
        for i in range(10):
            try:
                response = requests.get(link, timeout=30)
            except requests.exceptions.RequestException as e:
                print(e)
                time.sleep(5)
            else:
                response = response
                break

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            video_info = soup.find('iframe')['src']
            video_info = video_info.split('//www.youtube.com/embed/', 1)[1]

            video_title = soup.find('h1', class_='entry-title').get_text()
            video_title = video_title.split(' Video Download HD', 1)

            if video_info == youtube_code_previous:
                break

            t.append(video_info)
            d.append(video_title[0])


if len(d) > 0:
    with open(PATH+'youtube_code_hindi.txt', 'w') as f:
        for item in t:
            f.write('%s\n' % item)

    with open(PATH+'youtube_title_hindi.txt', 'w') as f:
        for item in d:
            f.write('%s\n' % item)

    firebase_conn_hindi.call()

else:
    print('No New Song to upload')
