#coding=utf-8

import os
import codecs
import configparser

#获取文件的真实路径，然后分割路径和文件名存入一个元组
proDir = os.path.split(os.path.realpath(__file__))[0]
#获取上层目录
parDir = os.path.dirname(proDir)
configPath=os.path.join(parDir,"config.ini")
print('---',configPath)

class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding="utf-8-sig")

    def get_email(self,name):
        value = self.cf.get("EMAIL",name)
        return value
    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value
    def get_db(self,name):
        value = self.cf.get("DATABASE",name)
        return value
if __name__ == '__main__':
    r = ReadConfig()
    print(r.get_email('mail_host'))