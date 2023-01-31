import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_1743157.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data.decode())
tree = ET.fromstring(data)

comments = tree.findall('comments')
comment = comments[0].findall('comment')

c=0
for i in range(0,len(comment)):
    c+=int(comment[i].find('count').text)
