#coding = utf-8

import requests

class Request_h():

    def __init__(self,url,data,request_type):
        self.url = url
        self.data = eval(data)
        self.request_type = request_type

    def http_request(self):
        urlstr = self.url
        payload = self.data
        if self.request_type=='post':
            r = requests.post(url=urlstr, data=payload)
            #r_text = r.text
        elif self.request_type=='get':
            r = requests.post(url=urlstr, params=payload)

        #r_text = r.text
        return r
xls_value = ['https://www.wanandroid.com/user/login', 'login', 'post', "{'username':'liangchao','password':'123456'}", '0']
case1 = Request_h(xls_value[0],xls_value[3],xls_value[2])
print(xls_value[0],xls_value[3],xls_value[2])
r_text = case1.http_request()
print(r_text)

