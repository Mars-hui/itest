#coding = utf-8
import unittest,json
from ddt import ddt,data,unpack
from common import readExcell
import requests
from common import configHttp1

'''教学'''

readexcel = readExcell.ReadExcel()
el = readexcel.excleList()
print("----", el)
datalist = []

for ele in el:
    elelist = [ele[1], ele[3], ele[4], ele[5]]
    datalist.append(elelist)
# print(datalist)

@ddt
class TestCase1(unittest.TestCase):

    # print(datalist)
    @data(*datalist)
    @unpack
    def test_normal(self,url,method,data,expect):
        req = configHttp1.ConfigHttp()
        res = req.getRequest(method,url,data)
        print('---',res)
        print(type(res))
        # real = res['errorCode']
        # print(real)
        # real = str(json.loads(res)['errorCode'])
        # try:
        #     # status=self.assertEqual(1,1)
        #     status = self.assertEqual(real,expect)
        #     status = 'Success'
        #     print('返回结果',status)
        # except AssertionError as msg:
        #     print(msg)
        #     status='Error'
        #     print('返回结果',status)
        #

if __name__ == '__main__':
    unittest.main()