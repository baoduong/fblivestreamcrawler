from bs4 import BeautifulSoup
import requests
# 1382841532216275_1382841888882906
# https://www.facebook.com/100068724216478/videos/762101395514448
# url = 'https://www.facebook.com/100068724216478/videos/1382841532216275?comment_id=1382841888882906'
url = 'https://m.facebook.com/100068724216478/videos/762101395514448?comment_id=1257373721542452'
# M8.21.0902074489
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
f = open("html/demofile.html", "a")
f.write(soup.prettify())
f.close()
# print(r.text)


# https://www.facebook.com/100068724216478/videos/762101395514448/?comment_id=925211291841064&__cft__[0]=AZW7czShhC0tEnFo9aUmPVglulwAuIfM_mfxTMCPZ6gQBKZeEpF-DkvOTXq1NBq3XrMT6xB44UWOzM3Q931o9lbjbDW0ihwdQoZG9E10xZzkA51wBnGlvdPKQe-aHuqMP4HDmUEPSXGeS_d2qxqbZJ6QCdUH-B5FcggutnxeW0wjaPE2TMmc55UrFK0aq0nHAFA&__tn__=R]-R