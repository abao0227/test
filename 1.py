# -*- coding=utf8 -*-

import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.baidu.com')
content = req.content
soup = BeautifulSoup(content,'html.parser')
alla =  soup.find_all('a')
for link in alla:
	print link.get('href')

#soup.get_text()
