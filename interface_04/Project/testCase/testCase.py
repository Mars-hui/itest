#coding=utf-8
from common import readExcel,confighttp
from common.writeExcel import writeExcel
from ddt import *
import unittest
import requests

@ddt
class TestCase(unittest.TestCase):
    # 1、获取数据
    a = readExcel.ReadExcel()
    excel_list = a.getExcelList()
    # print(type(excel_list))
    # print(excel_list)
    #2、发送请求
    @data(*excel_list)
    @unpack
    def test_normal(self,id,url,path,method,data,expect):

        print(id,url,path,method,data,expect)
        res = confighttp.GetResponse().sendRequest(method,url,data)
        print("返回",res)
        real = res['errorCode']
        print(real,expect)

    #3、断言结果
        wr = writeExcel()
        try:
            self.assertEqual(str(real),str(expect))
            reaslt='Success'
            print(reaslt)

        except AssertionError as m:
            reaslt='Error'
            print(reaslt)

    #4、写入文件
        print('info',id, real, reaslt,type(id),type(real),type(reaslt))
        wr.writeData(int(id), real, reaslt)


if __name__ == '__main__':
    unittest.main()


