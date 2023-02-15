import string
from tokenize import String
from bs4 import BeautifulSoup
import requests
from _config import pageId
import json
# f = open("html/demofile4.html", "r")
# fileDOc = f.read();
# soup = BeautifulSoup(fileDOc, 'html.parser')
# script =soup.find('script')
# print(script.text)


def crawler_userinfo(commend_id: String):
    _id = commend_id.split('_')
    url = 'https://www.facebook.com/{pageId}/videos/{videoId}?comment_id={id}'.format(
        pageId=pageId, videoId=_id[0], id = _id[1])
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    script = soup.find('script')
    # print(script.text)
    json_data = json.dumps(script.text)
    return json_data
