#coding=utf-8

import requests

# urlstr='https://www.wanandroid.com/article/query?k=Android'
# r = requests.get(url=urlstr)
# print(r.text)

'''方法二， 传成参数调用'''
# urlstr='https://www.wanandroid.com/article/query'
# payload = {
#     'k':'Android'
# }
# r = requests.get(url=urlstr,params = payload)

'''相应形式为gzip格式，则需用.content解码'''
urlstr = 'http://www.baidu.com'
r =requests.get(url=urlstr)
print(r.text)
print(r.content)
print(r.status_code)
print(r.headers)
print(r.cookies)
#print(r.json())
print(r.raw)