from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = input(' Enter ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retriev all of the achor tags
tags = soup ('a')
for tag in tags:
    print(tag.get('href', None))