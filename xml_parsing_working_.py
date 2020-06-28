import xml.etree.ElementTree as ET
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_696641.xml'
response = urllib.request.urlopen(url).read()
tree = ET.fromstring(response)

count = 0

for docTitle in tree.findall('.//count'):
    print(type(docTitle.text))
    count += int(docTitle.text)
    # print(num)

print(count)
    

   