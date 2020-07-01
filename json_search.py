# import xml.etree.ElementTree as ET
import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_696642.json'
response = urllib.request.urlopen(url).read()
tree = json.loads(response)

# print(tree)
totalnum = 0

for item in tree['comments']:
    print(item['count'])
    totalnum += int(item['count'])

print(totalnum)




# for docTitle in tree.findall('.//count'):
#     print(type(docTitle.text))
#     count += int(docTitle.text)
#     # print(num)

# print(count)
    

   