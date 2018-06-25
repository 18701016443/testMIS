#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/25 15:25
"""
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import unittest
import os,time

#定义发送邮件

def send_mail(file_new):
    f = open(file_new,"rb")
    mail_body = f.read()
    f.close()

    #以附件的形式发送邮件
    att = MIMEText(mail_body, "base64", "gbk")
    att["Content-Type"] = "application/octet-stream"
    file_name = file_new.split(r"./report/")[1]
    print(file_name)
    att["Content-Disposition"] = "attachment;filename="+file_name
    msgRoot = MIMEMultipart("related")
    msgRoot["Subject"] = "自动化测试报告"
    #邮件正文
    # msgRoot.attach(MIMEText("蚂蚁PC自动化测试报告，请查收~~","plain","utf-8"))
    msgRoot.attach(MIMEText(mail_body,"html","gbk"))
    msgRoot.attach(att)

    msgRoot["From"] = "18701016443@163.com"
    msgRoot["To"] = "zhangjiaheng@iyoujia.com"
    # msgRoot["From"] = "bxj3416162@163.com"
    # msgRoot["To"] = "buxiangjie@huirendai.net"


    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("18701016443", "zjh18701016443")
    smtp.sendmail("18701016443@163.com", "zhangjiaheng@iyoujia.com", msgRoot.as_string())
    smtp.quit()
    print("email has send out")


    #以下是以html模式发送的邮件
    # msg = MIMEText(mail_body,"html","utf-8")
    # msg["Subject"] = Header("自动化测试报告","utf-8")
    #
    # msg["From"] = "18701016443@163.com"
    # msg["To"] = "zhangjiaheng_dz@mayi.com"
    #
    # smtp = smtplib.SMTP()
    # smtp.connect("smtp.163.com")
    # smtp.login("18701016443","zjh18701016443")
    # smtp.sendmail("18701016443@163.com","zhangjiaheng_dz@mayi.com",msg.as_string())
    # smtp.quit()
    # print("email has send out")

#查找测试报告目录，找到最新生成的测试报告文件

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = r"./report/"+ now +"result.html"

    fp = open(filename,"w")
    runner = HTMLTestRunner(stream=fp,
                            title="PC自动化测试报告",
                            description="环境 win10  浏览器：谷歌/65版")

    discover = unittest.defaultTestLoader.discover(r"./test_cases/",
                                                   pattern="test_*.py")

    runner.run(discover)
    fp.close()
    file_path = new_report(r"./report/")
    send_mail(file_path)
