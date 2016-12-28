import requests
req = requests.get('https://www.baidu.com')
requests.
print req.headers['content-type']
print req.encoding
print req.content
#print req.text