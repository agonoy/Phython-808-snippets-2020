import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input(' http://py4e-data.dr-chuck.net/comments_696639.html')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
