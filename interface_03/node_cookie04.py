#coding=utf-8
import requests,re
'''3.定制cookie，单独设置cookie来访问目标值'''

urlstr = 'https://www.wanandroid.com/user/login'
payload = {
    'username': 'chaoge',
    'password': '123456'
}
r = requests.post(url=urlstr,data=payload)
print('*****',r.text)
print('*****',r.cookies)
print('*****',r.headers)
print(r.cookies['JSESSIONID'])
header={
    'cookie':'JSESSIONID='+r.cookies['JSESSIONID']
    }
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',headers=header)
print('*****',r2.text)
print('****',r2.headers)
result = r2.text.find("已完成清单")
print(result)
if result != -1:
    print("查询成功")
else:
    print('查询失败')

pattern = re.compile(r';\">(.*?)<\/h2>')
result = pattern.findall(r2.text)
print(result)
