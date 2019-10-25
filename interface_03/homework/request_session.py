#coding=utf-8
import requests,json
'''
如何保持回话：
    使用session（）函数，自动携带上次的cookie信息。
'''
urlstr = 'https://www.wanandroid.com/user/login'
payload = {
    'username':'chaoge',
    'password':'123456'

}
s = requests.session()
r = s.post(url = urlstr,data=payload)
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')

