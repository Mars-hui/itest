#coding = utf - 8
import os
import unittest
import time
import HTMLTestRunner

class runAll(object):
    def run_case(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        case_dir = proDir + '\\testcase'
        # print(case_dir)
        discover = unittest.defaultTestLoader.discover(
            case_dir,
            pattern = '*Test.py',
            top_level_dir=None
        )
        return discover

if __name__ == '__main__':
    #时间戳
    current_time = time.strftime("%Y-%M-%d-%H_%M_%S", time.localtime(time.time()))
    proDir = os.path.split(os.path.realpath(__file__))[0]
    case_dir = proDir + '\\report\\'
    report_dir = case_dir+current_time+".html"
    print(report_dir)
    #生成报告
    fp = open(report_dir,'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'app自动化测试报告',
        description=u'XX接口'
    )
    runner.run(runAll.run_case())
    fp.close()


    # r = runAll()
    # r.run_case()