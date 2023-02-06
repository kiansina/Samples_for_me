from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_1743158.json'

response = urlopen(url)

data = json.loads(response.read())


c=0
for i in data['comments']:
    c+=int(i['count'])
