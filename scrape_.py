import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url_data = input("Enter URL")
openUrl = urllib.request.urlopen(url_data).read()
mysoup = BeautifulSoup(openUrl, 'html.parser')
print(mysoup)

tags = mysoup('a')
for tag in tags:
    print(tag.get('href', None))

print('deso it wiasf')

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in openUrl:
    # print(line.decode().strip())
    rawtags = line.decode().strip().read()

    print(rawtags)
