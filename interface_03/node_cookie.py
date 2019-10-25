#coding=utf-8
#必须熟练
import requests
'''1. 手动获取上已请求返回的cookie，用在下次请求中'''

urlstr = 'https://www.wanandroid.com/user/login'
payload = {
    'username': 'chaoge',
    'password': '123456'
}
r = requests.post(url = urlstr,data = payload)
print('*',r.text)
print('*',r.cookies)
print('*',r.headers)

cookie = r.cookies

r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)


