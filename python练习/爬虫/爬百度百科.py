from bs4 import BeautifulSoup
from urllib.request import urlopen
# import urllib
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E5%85%A8%E8%81%8C%E9%AB%98%E6%89%8B/6893637"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features="html.parser")
    print(soup.find('h1').get_text(), '     url:', his[-1])

    sub_urls = soup.find_all("a",
                             {
                                 "target": "_blank",
                                 "href": re.compile(("/item/(%.{2})+$"))
                             })
    # print(sub_urls)
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()
    # print(his)


