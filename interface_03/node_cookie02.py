#coding=utf-8
import requests
'''2.通过requests.session自动设置cookie'''

urlstr = 'https://www.wanandroid.com/user/login'
payload = {
    'username': 'chaoge',
    'password': '123456'
}
s = requests.session()
r = s.post(url = urlstr,data=payload)

r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')

print('***',r2.text)
print('****',r.text)