import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_web_image('http://apikabu.ru/img_n/2012-10_1/a51.jpg')