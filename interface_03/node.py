#coding = utf-8
import requests

#练习get请求
#发送get请求：
url_str='https://blog.csdn.net/rainshine1190'
#访问网址
html = requests.get(url_str)
print(html)#返回的内容为响应状态码
print(html.text)
'''get请求携带参数'''
url_str_02 = 'https://www.wanandroid.com/article/query?k=Android'
r = requests.get(url = url_str_02)
print(r.text)
'''方法二，将get中的参数写单独写'''
# url_str_03 = 'https://www.wanandroid.com/article/query'
# payload = {
#     'k':'Android'
# }
# r = requests.get(url = url_str_03,data = payload)
# print(r.text)
# print(r.status_code)# 返回200说明地址

'''响应内容是gzip压缩的，并非文本'''
# r = requests.get('https://www.baidu.com')
# print("url:"+r.url)
# #print(r.text)
# print("编码："+r.encoding)  #编码
# print(r.content) #获取返回内容
# print(r.headers)
# print(r.cookies)
# #print(r.json())
# print(r.raw)
# print(r.text)
# print(r.raise_for_status())
