#coding=utf-8

import requests,json
payload = {
    'yoyo':True,
    'json':False,
    'python':'22222'
}
print(type(payload))
print(type(json.dumps(payload)))