# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

c=0
for i in range(0,7):
    if c==0:
        url ='http://py4e-data.dr-chuck.net/known_by_Mobeen.html'
    else:
        url =tag.get('href', None)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    tag=tags[17]
    print(tag.contents[0])
    c+=1
