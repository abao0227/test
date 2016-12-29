# -*- coding=utf8 -*-
import requests
from bs4 import BeautifulSoup
import json

json_string = {
    "success": "1",
    "info": "成功",
    "data": {
        "list": [
            {
                "word": "淘宝seo",
                "total": 239
            },
            {
                "word": "哪里学seo",
                "total": 0
            }
        ]
    }
}

s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]