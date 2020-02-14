#coding = utf - 8

from common.readconfig import readConfig
import os
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart

class ConfigEmail(object):
    #获得发件人邮箱，用户名，密码
    r = readConfig()
    mail_host = r.get_email('mail_host')
    mail_host = r.get_email('mail_host')
    mail_host = r.get_email('mail_host')

    # 配置邮件属性
    sender = r.get_email('sender')
    receivers = r.get_email('receiver')
    content = r.get_email('content')
    msg = MIMEMultipart()
    print("mag",msg)

    def config_file(self):
        file = self.find_file()
        send_file = open(file, 'rb').read()
        att = MIMEText(send_file, 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] ='attachment;filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.mail_user
        self.msg['To'] = self.sender
        self.msg['Subject'] = Header()
        self.msg.attach(MIMEText('这是接口自动化报告邮件，如果想查看详情请查收附件', 'plain', 'utf-8'))

    def find_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        report_path = os.path.dirname(current_path) + '//report'
        # print(report_path)
        report_list = os.listdir(report_path)
        # print(report_list)

        file_time = []
        time_name_dic = {}

        for iName in report_list:
            file_name = report_path + '/' + iName
            ele_time = os.path.getmtime(file_name)
            file_time.append(ele_time)
            time_name_dic[ele_time] = iName

        # maxTime = max(file_time)
        new_file = time_name_dic[max(file_time)]
        send_file = report_path + '/' + new_file
        return send_file

    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP_SSL(self.mail_host, 465)
            s.ehlo()
            s.login(self.sender, self.receivers, self.msg.as_string())
            s.close()
            print('邮件发送成功')
        except smtplib.SMTPException as msg:
            print('Error:无法发送邮件')


if __name__ == '__main__':
    c = ConfigEmail()
    c.find_fiel()



'''【总结：os的部分用法】
1. 获取当前目录：os.path.abspath(__file__)---E:\training\code\vip3test\project_appm\common\configEmail.py
2. 获取上级路径：os.path.dirname(path)---E:\training\code\vip3test\project_appm\common
3. 获取目录下的文件：os.listdir(path)

'''
