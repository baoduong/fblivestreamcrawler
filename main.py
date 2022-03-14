from bs4 import BeautifulSoup
import requests
# 1382841532216275_1382841888882906
url = 'https://www.facebook.com/102280315741900/videos/1382841532216275?comment_id=1382841888882906'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
f = open("html/demofile4.html", "a")
f.write(soup.prettify())
f.close()
# print(r.text)