"""Practice using urllib"""

from urllib import request

#print(dir(request))

req = request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
print(req,req.code,req.length)
#print(req.peek())
byte = req.read()
html = byte.decode('UTF-8')
print(type(byte))
print(html)