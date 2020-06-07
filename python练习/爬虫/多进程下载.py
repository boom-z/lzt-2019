import multiprocessing as mp
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}

param = {
    "c": "WallPaper",
    "start": "1",
    "count": "20",
    "from": "360chrome",
    "a": "getAppsByCategory",
    "cid": "9"
}
html = requests.get(
    'https://cors.zme.ink/http://wallpaper.apc.360.cn/index.php',
    params=param,
    headers=headers
).text

html = json.loads(html)
# print(html['data'])
# [print(url['url']) for url in html['data']]


def crawl(imgurl):
    # print(imgurl)
    img_name = imgurl.split('/')[-1]
    r = requests.get(imgurl, stream=True)
    with open("./img2/%s" % img_name, "wb") as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)
    print('saved %s' % img_name)
    return imgurl


if __name__ == '__main__':
    pool = mp.Pool(4)
    imgs = [pool.apply_async(crawl, args=(url['url'],)) for url in html['data']]
    results = [j.get() for j in imgs]
