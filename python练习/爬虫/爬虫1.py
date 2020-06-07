from urllib.request import urlopen


html = urlopen(
    "https://blog.csdn.net/lancegentry/article/details/79381047"
).read().decode('utf-8')
# print(html)

