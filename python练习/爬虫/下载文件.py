from bs4 import BeautifulSoup
from urllib.request import urlretrieve

import requests

# 方法一
# img_url = "https://imgs.aixifan.com/Fp72Es_8ibSz2e4651z6GON9PdQm"
# urlretrieve(img_url, './img/image1.png')

# 方法二
# r = requests.get("https://imgs.aixifan.com/Fl9ADdWVCoiDIB4AyPOoU06AYVbR")
# with open("./img/image2.png", "wb") as f:
#     f.write(r.content)

# 下载大文件（流文件）
r = requests.get("https://imgs.aixifan.com/Fl9ADdWVCoiDIB4AyPOoU06AYVbR", stream=True)
with open("./img/image4.png", "wb") as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
