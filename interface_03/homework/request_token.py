#coding=utf-8
import requests,json

urlstr = ''
payload={

}
s=requests.session()
r = s.post()
token = r.json()['token']

header={}
header['token']=token
r2 = s.post()