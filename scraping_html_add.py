# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_696639.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total_num = 0;
# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    
    # getting the number out
    # findall_num = re.findAll('[0-9]+',tag)
    number_stripped = re.findall('[0-9]+', str(tag))
    for x in number_stripped:
        # print(int(x))
        total_num += int(x)
print(total_num)