#coding = utf-8
import requests,json,re

'''携带cookie请求的方法有4种'''
#1、手动获取上一请求返回的cookie值设置下次请求cookie
#get 中携带cookie ，在后边加cookies=
urlstr = ''
payload = {

}
r = requests.post(url = urlstr,data=payload)
cookie = r.cookies
r2 = requests.get(url ='',cookies = cookie)

#2、通过session()函数自动设置cookie完成访问
urlstr = ''
payload = {

}
s = requests.session()
r = s.requests(url = urlstr,data = payload)
r2 = s.get()

#3、通过定制cookie，单独设置cookie访问目标网址
r = requests.post(url = urlstr,data = payload)
cookie={
    'JSESSIONID':r.cookies['JSESSIONID']
}
r2 =requests.get(url = urlstr,cookies = cookie)

#4、通过定制cookie，放入header来访问目标网址
urlstr = ''
payload ={

}
r = requests.post(url = urlstr,data=payload)
print(r.cookies['JSESSIONID'])
header = {
    'cookie':'JSESSIONID='+r.cookies['JSESSIONID']

}
r2 = requests.get(url = '',headers = header)
result = r2.text.find('已完成清单')
if result != -1:
    print('查询成功')
else:
    print('查询失败')

#或通过正则来查找
pattern = re.compile(r';\">(.*?)<\/h2>')