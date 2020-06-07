
import requests
from bs4 import BeautifulSoup


from urllib.request import urlopen
import urllib

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}

param = {"search": "angels of death"}
html = requests.get('https://wall.alphacoders.com/search.php', params=param, headers=headers).text
# print(html)
soup = BeautifulSoup(html, features="html.parser")
img_list = soup.find_all('div', {"class": "thumb-container-big"})
# print(img_url)
for i in img_list:
    img = i.find('img')
    if(img.get('data-src')!=None):
        url = img.get('data-src')
        url_all = url.split('thumb')
        url_end = url_all[-1].split('-')[-1]
        new_url = url_all[0] + url_end
        print(new_url)
        r = requests.get(new_url, stream=True)
        img_name = url_end
        with open("./img/%s" % img_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('saved %s' % img_name)