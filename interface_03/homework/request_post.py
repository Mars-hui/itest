#coding=utf-8
import requests,json
'''post请求中url,header,data/json,若请求的body为json格式则传json，若为表单格式则用data'''

# urlstr = 'http://httpbin.org/post'
#
# payload = {
#     'qq群名': 'selenium',
#     'qq群号': '106014970'
#
# }
# payload = json.dumps(payload)
# r = requests.post(url = urlstr,data = payload)
# print(r.text)

'''方法二，直接用json='''

# urlstr = 'http://httpbin.org/post'
#
# payload = {
#     'qq群名': 'selenium',
#     'qq群号': '106014970'
#
# }
#
# r = requests.post(url = urlstr,json = payload)
# print(r.text)

'''请求中携带header'''
urlstr = 'https://www.wanandroid.com/user/login'
header = {
    'User-Agent':'Mozilla/6.0'
}
payload = {
    'username':'chaoge',
    'password':'123456'
}

r = requests.post(url = urlstr,headers = header,data = payload)

print(r.text)
print(r.json()['data']['admin'])
if r.json()['data']['username']==payload['username']:
    print('成功')

