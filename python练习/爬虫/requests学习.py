import requests
import webbrowser

param = {"wd": "全职高手"}
r = requests.get('https://www.baidu.com/s', params=param)
print(r.url)
webbrowser.open(r.url)

