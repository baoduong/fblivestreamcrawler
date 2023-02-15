from bs4 import BeautifulSoup
import requests
# 1382841532216275_1382841888882906
# https://www.facebook.com/100068724216478/videos/762101395514448
# url = 'https://www.facebook.com/100068724216478/videos/1382841532216275?comment_id=1382841888882906'
url = 'https://www.facebook.com/100068724216478/videos/762101395514448?comment_id=1257373721542452'
# M8.21.0902074489
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
f = open("html/demofile.html", "a")
f.write(soup.prettify())
f.close()
# print(r.text)