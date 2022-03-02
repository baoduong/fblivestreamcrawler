from bs4 import BeautifulSoup
import requests

url = 'https://www.facebook.com/102280315741900/videos/331805768913394?comment_id=331806575579980'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
f = open("html/demofile2.html", "a")
f.write(soup.prettify())
f.close()
# print(r.text)