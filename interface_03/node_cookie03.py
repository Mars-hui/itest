#coding=utf-8
import requests
'''3.定制cookie，单独设置cookie来访问目标值'''

urlstr = 'https://www.wanandroid.com/user/login'
payload = {
    'username': 'chaoge',
    'password': '123456'
}
r = requests.post(url=urlstr,data=payload)
print(r.cookies['JSESSIONID'])

cookie={
    'JSESSIONID':r.cookies['JSESSIONID']
}

r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)
print('*****',r2.text)
print('****',r2.headers)

