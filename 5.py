# -*- coding=utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests
from bs4 import BeautifulSoup
import json

res = requests.get('http://fund.eastmoney.com/dingtou/syph_yndt.html')
res.encoding = 'utf-8'
content = res.text
soup = BeautifulSoup(content,'html.parser')
thead_tr = soup.select('#lbtable thead tr')
tbody_tr = soup.select('#lbtable tbody tr')
#print input_str
yyy = []
for i in thead_tr:
    #y = {}
    y2 = ''
    for x in xrange(1,13):
        y =  i.select('th')[x].text
        y2 = y2 + y
        yyy.append(y)
    #print y2
print yyy  
#print yyy[0]  

zzz = []
for i in tbody_tr:
    #y = {}
    z2 = ''
    for x in xrange(1,13):
        z =  i.select('td')[x].text
        z2 = z2 + z
        zzz.append(z)
print zzz 



    #print z2
    #for i2 in i.select('tr'):
        #print i2.select('th')[0].text
#print sel
#print soup.select('#lbtable tbody tr a')[0]
#print sel.find(a[href])
#for i in input_str:
