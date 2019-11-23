#coding=utf-8

from test_Unittest import Count
import unittest,os
import HTMLTestRunner


class RunAll():
    dir = os.getcwd()
    # print(dir)
    discover = unittest.defaultTestLoader.discover(dir,pattern="test*.py",top_level_dir=None)

    runner = unittest.TextTestRunner()


    filename = dir+"\\testCount.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'计算测试报告',
        description=u'用例执行情况：'
    )
    runner.run(discover)
    fp.close()






