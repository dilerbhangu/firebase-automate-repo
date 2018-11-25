import requests
from bs4 import BeautifulSoup
# <ul class="videoInfoList">
# 	<li><a href="https://www.youtube.com/watch?v=kQHuiTDTvYk" target="_break">YouTube <i class="icon-external-link"></i></a></li>
# </ul>

url='https://imvdb.com/new/'
header={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response= requests.get(url,header)
soup=BeautifulSoup(response.content,'html.parser')
songs_list=soup.find('div',class_='rack_node')
if response.status_code!=200:
    print(response.status_code)
else:
    x=songs_list.findNext('a')
    print(x['href'])
