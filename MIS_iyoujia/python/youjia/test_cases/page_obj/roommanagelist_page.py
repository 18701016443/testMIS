#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/20 16:36
"""

from .base import Pyse

#房源管理列表

class RoomManageListPage(Pyse):

    #房源ID_搜索
    def SelectID(self,id):
        self.type("xpath=>//*[@id='pane-fyList']/div/div[1]/div/div[1]/div[3]/div/input",id)

    #去掉wujiaqu
    def wujiaqu(self):
        self.click("xpath=>//*[@id='pane-fyList']/div/div[2]/h3/label/span[1]/span")

    #房源名称
    def RoomName(self,name):
        self.type("id=>",name)

    #城市
    def City(self):
        self.click("id=>")

    #站名称
    def Site(self):
        self.click("id=>")

    #列表_房源状态
    def RoomState(self):
        text = self.get_text("xpath=>//*[@id='pane-fyList']/div/div[2]/div[1]/div[3]/table/tbody/tr/td[9]/div")
        return text

    #房源ID
    def RoomId(self):
        self.open_new_window("xpath=>//*[@id='pane-fyList']/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div/span")

    #编辑
    def Eidt(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[2]/div[1]/button/span")

    #房源简介
    def RoomIntroduce(self,introduce):
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[4]/div/div/form/div[3]/div/div/div/div/div/textarea",introduce)


    #基础低价
    def FloorPrice(self,price):
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[5]/div/div/form/div[1]/div/div/div/div/input",price)

    #周末类型_不设置
    def NoSetUp(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[5]/div/div/form/div[2]/div/div/div/div/label[4]/span[1]/span")


    #押金
    def yajin(self,num):
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[5]/div/div/form/div[3]/div/div/div/div/input",num)

    #可住人数
    def pople(self,p):
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[6]/div/div/form/div[6]/div/div/div/div/input",p)

    #其他须知
    def Other(self,other):
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[6]/div/div/form/div[13]/div/div/div/div/div/textarea",other)

    #提交
    def Submit(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[2]/div[1]/button/span")

    #通过
    def Pass(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[2]/div[1]/button")

    #二次确认
    def TwoPass(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[2]/span")

    # 退款政策——渠道
    def SelectRefundChannel(self,i):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[5]/div/div/form/div[4]/div/div/div/div/div[1]/label["+i+"]/span")

    #退款政策——支持Or宽松
    def SelectRefund(self,i="1"):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[5]/div/div/form/div[4]/div/div/div/div/div[2]/div/div["+i+"]/label/span[1]/span")



