#coding = utf-8
import requests

class GetResponse():
    def sendRequest(self,method,url,data):
        if str(method) == 'post':
            res = self.sendPost(url,data)
        else:
            res = self.sendGet(url,data)
        return res

    def sendPost(self,url,data):
        url_str = url
        payload = eval(data)
        re = requests.post(url=url_str, data=payload)
        return re.json()

    def sendGet(self,url,data):
        url_str = url
        payload = eval(data)
        re = requests.get(url=url_str, params=payload)
        return re.json()