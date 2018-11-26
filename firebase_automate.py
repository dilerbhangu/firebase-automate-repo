import requests
from bs4 import BeautifulSoup

url='https://imvdb.com/new/'
header={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response= requests.get(url,header)
soup=BeautifulSoup(response.content,'html.parser')
songs_list=soup.find_all('div',class_='rack_node')
songs_link=[]
d=[]
t=[]
if response.status_code!=200:
    print(response.status_code)
else:
    for i in range(0,3):
        link=songs_list[i].findNext('a')
        songs_link.append(link['href'])

    for link in songs_link:
        response=requests.get(link,header)
        if response.status_code!=200:
            print(response.status_code)
        else:
            soup=BeautifulSoup(response.content,'html.parser')
            video_title=soup.find('div',id='videoTitle')
            video_info=soup.find_all('ul',class_='videoInfoList')
            s1=video_title.findNext('h1').text
            s1=s1.split(' \t',1)[0]
            d.append(s1)

            s2=video_info[-1].findNext('a')
            s2=s2['href']
            s2=s2.split('https://www.youtube.com/watch?v=',1)[1]
            t.append(s2)


print(d)
print(t)
