from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
req = urllib.request.Request(url="https://www.bilibili.com/", headers=headers)

html = urlopen(req).read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features="html.parser")
# print(soup.h1)
# print('\n', soup.title)
#
all_href = soup.find_all('a')
# print(all_href)
for l in all_href:
    if(l.get('href') != None):
        print('https:' + l.get('href'))
        # print(l.get('href'))
