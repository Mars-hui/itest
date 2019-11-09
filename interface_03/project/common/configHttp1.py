#coding = utf-8
import requests
class ConfigHttp():

    def getRequest(self,method,url,data):
        if method=='post':
            return self.sendpost(url,data)
        else:
            return self.sendget(url,data)

    def sendpost(self,url,data):
        urlstr = url
        payload = eval(data)
        response = requests.post(url=urlstr,data=payload)
        res = response.text
        return res

    def sendget(self,url,data):
        urlstr = url
        payload = eval(data)
        response = requests.post(url=urlstr,params=payload)
        res = response.text
        return res
