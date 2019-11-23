#coding = utf-8
import unittest,os
import time
import HTMLTestRunner
from common import configEmail

def run_case(dir = "testCase"):
    case_dir = os.getcwd()+"\\testCase"
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern="test*.py",
        top_level_dir=None
    )
    return discover

# def clear_report():
#     report_path = os.getcwd()+"\\report"
#     fileList = os.listdir(report_path)
#     print(fileList)
#     print(len(fileList))
#     while len(fileList)>3:
#
#
#
#
#     if len(fileList) > 5:
#         for i in fileList:
#             re_p = report_path+"/"+i
#             os.remove(re_p)
#
#     fileNewList = os.listdir(report_path)
#     print(fileNewList)

# clear_report()



if __name__ == '__main__':
    #取时间戳
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    report_dir = os.getcwd()+"\\report\\"+current_time+".html"
    print(report_dir)
    #生成报告
    fp = open(report_dir,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title = u'接口自动化测试报告',
        description= u'XX接口',
        verbosity=2
    )
    runner.run(run_case())
    fp.close()
    #发送邮件
    c = configEmail.ConfigEmail()
    c.send_mail()



