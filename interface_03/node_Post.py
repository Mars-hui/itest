#coding = utf-8
import json,requests

# urlstr = 'http://httpbin.org/post'
# payload ={
#     'qq群名':'selenium+jmeter+loadrunner',
#     'qq群号':'106014970'
# }
# payload = json.dumps(payload)
#
# r = requests.post(url = urlstr,data = payload)

#示例2
'''当接口body为json时，则requests.post中的第二个参数指定json=而不是data'''
# urlstr = 'http://httpbin.org/post'
# payload = {
#     'qq群名':'selenium+jmeter+loadrunner',
#     'qq群号':'106014970'
#
# }
# r = requests.post(url = urlstr,json = payload)
# print(r.text)
# print(r.json())

'''包含请求头headers的请求发送'''
#示例1
# urlstr = 'https://www.wanandroid.com/user/login'
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
# }
# payload = {
#     'username':'chaoge',
#     'password':'123456'
# }
# r = requests.post(url = urlstr,headers = header,data = payload)
# print(r.text)
# print(r.headers)

#示例2
urlstr = 'https://www.wanandroid.com/user/login'
payload = {
    'username':'chaoge',
    'password':'123456'
}
r = requests.post(url = urlstr,data = payload)

print(r.text)
print(type(r.json()))
print(r.json()['data']['username'])
#print()
print(r.json()['data']['admin'])



