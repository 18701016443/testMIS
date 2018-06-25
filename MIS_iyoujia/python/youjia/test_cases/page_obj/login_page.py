#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/14 9:10
"""

from .base import Pyse
from time import sleep
from models import configdb



#登录页面定位

class LoginPage(Pyse):

    url = ""

    """
    账号密码登录
    """
    #手机号
    def P_Phone(self,phone):
        self.type("xpath=>//*[@id='app']/div/div/div/div[2]/section[1]/form/div[1]/div/div/input",phone)

    #密码
    def P_password(self,password):
        self.type("xpath=>//*[@id='app']/div/div/div/div[2]/section[1]/form/div[2]/div/div/input",password)

    #图片验证码
    def P_PictureCode(self,code):
        self.type("xpath=>//*[@id='app']/div/div/div/div[2]/section[1]/form/div[3]/div/div[1]/input",code)

    #登陆按钮
    def P_LoginBtn(self):
        self.click("xpath=>//*[@id='app']/div/div/div/div[2]/section[1]/form/div[4]/div/button/span")

    """
    手机验证码登录
    """
    def PhoneLogin(self):
        self.click("xpath=>//*[@id='app']/div/div/div/div[1]/div[2]")
    #登录手机号
    def LoginPhone(self,phone):
        # phone = 18301028337
        # phone = 18701016443
        self.type("xpath=>//*[@id='app']/div/div/div/div[2]/section[2]/form/div[1]/div/div/input",phone)

    #发送验证码按钮
    def SendCodeBtn(self):
        self.click("xpath=>//*[@id='app']/div/div/div/div[2]/section[2]/form/div[3]/div/div[2]/span")

    #图片验证码输入框
    def PictureCode(self):
        #测试环境使用
        pw = "aaaa"
        self.type("xpath=>//*[@id='app']/div/div/div/div[2]/section[2]/form/div[2]/div/div[1]/input",pw)
        #线上使用
        # self.click("xpath=>//*[@id='app']/div/section/form/div[2]/div/div[1]/input")


    #短信验证码输入框
    def MessageCode(self,msgcode):
        # self.click("xpath=>//*[@id='app']/div/section/form/div[3]/div/div[1]/input")
        self.type( "xpath=>//*[@id='app']/div/div/div/div[2]/section[2]/form/div[3]/div/div[1]/input",msgcode)
    #登录
    def Loginbtn(self):
        self.click("xpath=>//*[@id='app']/div/div/div/div[2]/section[2]/form/div[4]/div/button/span")

    #获取登录人姓名
    def LoginName(self):
        t = self.get_text("xpath=>//*[@id='right-box']/div/h1")
        return t


    # 其他页面调用使用
    def Login(self):
        self.open()
        sleep(2)
        # #手动登录
        self.PhoneLogin()
        sleep(1)
        self.LoginPhone(17601052158)
        self.PictureCode()
        sleep(1)
        self.SendCodeBtn()
        sleep(3)
        msg = configdb.cord(17601052158)
        sleep(2)
        msgcode = msg
        self.MessageCode(msgcode)
        sleep(1)
        self.Loginbtn()

