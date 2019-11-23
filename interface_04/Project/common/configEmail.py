#coding=utf-8
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import readconfig
import os

class ConfigEmail():
    # 读取ini文件配置属性
    r = readconfig.ReadConfig()

    # 配置第三方SMTP服务
    mail_host=r.get_email('mail_host')
    mail_user=r.get_email('mail_user')
    mail_pass = r.get_email('mail_pass')

    # 配置邮件属性
    sender = r.get_email('sender')
    receivers = r.get_email('receiver')
    content = r.get_email('content')
    msg = MIMEMultipart()
    print("mag",msg)

    #配置附件属性
    def config_file(self):
        file = self.find_file()
        # print(file)
        sendfile = open(file,'rb').read()
        att = MIMEText(sendfile,'plain','utf-8')
        # print(att)
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] ='attachment;filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.mail_user
        self.msg['To'] = self.sender
        self.msg['Subject'] = Header()
        self.msg.attach(MIMEText('这是接口自动化报告邮件，如果想查看详情请查收附件','plain','utf-8'))

    def find_file(self):
        #获取当前路径
        current_path = os.path.dirname(os.path.abspath(__file__))
        #获取报告的存放路径
        filePath = os.path.dirname(current_path)+"/"+'report'
        #获取filepath路径下全部文件名称的列表
        fileList = os.listdir(filePath)

        fileDict = {}
        fileTime = []

        for iName in fileList:
            #拼接文件路径和i-文件名
            filename = filePath+"/"+iName
            #获取文件的修改时间
            iTime = os.path.getmtime(filename)
            #将文件的修改时间追加到时间列表中
            fileTime.append(iTime)
            #将文件名iname作为字典的value，文件的修改时间iTime作为字典的key存入
            fileDict[iTime] = iName

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        sendfile = filePath+"/"+sendfile
        return sendfile
    #发送邮件
    def send_mail(self):
        self.config_file()
        try:
            # s = smtplib.SMTP()
            # s.connect(self.mail_host,25)
            s = smtplib.SMTP_SSL(self.mail_host,465)
            s.ehlo()
            s.login(self.mail_user,self.mail_pass)
            s.sendmail(self.sender,self.receivers,self.msg.as_string())
            s.close()
            print("邮件发送成功")
        except smtplib.SMTPException as msg:
            print("Error:无法发送邮件")

if __name__ == '__main__':

    c = ConfigEmail()
    c.send_mail()








