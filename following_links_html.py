# will go through a series of link. . .

# $ python3 solution.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
# The answer to the assignment for this execution is "Anayah".

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# NOTE: python 3.8.3 64-bit.


import bleach
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# position = int(input("Enter position: "))
# count = int(input("Enter count: "))

# def link_iterator(soup_tag, position_par, count_par):

    
#     return link
    
    
    
    
# global data
position_ = 18
count_ = 7
mybleach_data_ = []
url_storage_ = "http://py4e-data.dr-chuck.net/known_by_Shi.html"




for xx in range(count_):
    

    # url = input('Enter - ')
    url = url_storage_
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    
    
    
    
    
    
    
    total_num = 1
    num_of_iter = 0
    
    for tag in tags:
    # TODO: find the position whatever 
    # TODO: the position # is ( user input )
        if position_ == total_num:
            print('URL:', tag.get('href', None))
            first_link = tag.get('href', None)
            # print(type(first_link))
            url_storage_ = first_link;
            mybleach_data_.append(bleach.clean(tag.get_text(), strip=True))
            break
        
        total_num += 1

    # Look at the parts of a tag
    # print('TAG:', tag, " ", "type: ", type(tag))
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)


# ! 1.   using Bleach
    # soupa = BeautifulSoup(tag)

        # mybleach_data_.append(bleach.clean(tag.get_text(), strip=True))

    # remember. . tag is TAG.  the .get_text() converts it to text so bleach can use it.

# print(type(mybleach_data_))
print((mybleach_data_))

# get the last array

last_array = mybleach_data_[len(mybleach_data_)-1]
print(last_array)


# print(mybleach_data)
# ! END


# TODO #1: getting the number out
    # findall_num = re.findAll('[0-9]+',tag)
#     number_stripped = re.findall('[0-9]+', str(tag))
#     for x in number_stripped:
#         # print(int(x))
#         total_num += int(x)
# print(total_num)
# TODO #1 END
