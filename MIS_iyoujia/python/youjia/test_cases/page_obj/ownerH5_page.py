#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/18 16:11
"""

from .base import Pyse
from models import mydef
from selenium.webdriver.support.select import Select
from selenium import webdriver

"""PC业主招募H5"""

class OwnerH5(Pyse):

    #打开H5页面
    def openH5(self):
        self.opentest("http://www.iyoujia.com/")

    #成为业主
    def Owner(self):
        self.click("xpath=>//*[@id='indexPage']/div[2]/div/div/span")

    #姓名
    def OwnerName(self):
        name = "张佳恒测试"
        self.type("xpath=>//*[@id='name']", name)

    #手机号
    def OwnerPhone(self):
        phone = "17601052158"
        self.type("xpath=>//*[@id='phone']", phone)

    #图形验证码
    def OwnerPicture(self,LL):
        self.type("xpath=>//*[@id='loginimage']",LL)

    #短信验证码
    def OwnerMessageInput(self,msg):
        self.type("xpath=>//*[@id='dx_login']",msg)

    #获取验证码
    def OwnerMessage(self):
        self.click("xpath=>//*[@id='getloginphonecode']")

    #民居、公寓、别墅、客栈、其他
    def OwnerResidence(self):
        i = mydef.rad_num(1,6)
        self.click("xpath=>//*[@id='indexPage']/div[6]/div[2]/div[1]/div[5]/div/ul/li["+ i +"]/span")

    #房源套数
    def OwnerRoomNum(self):
        num = mydef.rad_num(1,999)
        self.type("xpath=>//*[@id='house_num']",num)

    #省
    def Province(self):
        self.click("xpath=>//*[@id='indexPage']/div[6]/div[2]/div[1]/div[7]/div[1]/div/div[1]/input")

    #利用js将滚动条拉倒最下面
    def xiugai(self,id):
        self.js("var q=document.getElementById('%s').scrollTop=9000"%id)
    #新疆
    def xinjiang(self):
        self.click("xpath=>//*[@id='province_select']/li[30]")

    #市——五家渠
    def wujiaqu(self):
        self.click("xpath=>//*[@id='city_select']/li[19]")

    def qu(self):
        self.click("xpath=>//*[@id='district_select']/li[1]")

    #详细地址
    def Address(self):
        address = "五家渠测试地址"
        self.type("xpath=>//*[@id='xx_address']",address)

    #提交
    def SubmitBtn(self):
        self.click("xpath=>//*[@id='indexPage']/div[6]/div[2]/div[2]")