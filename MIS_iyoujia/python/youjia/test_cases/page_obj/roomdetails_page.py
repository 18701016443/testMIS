#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/20 16:49
"""
from .base import  Pyse

#房源管理点击房源id进入——房源详情页

class RoomDetailsPage(Pyse):

    #房源标题
    def RoomTitle(self,title):
        self.type("id=>",title)

    #房源简介
    def RoomIntroduce(self,introduce):
        self.type("id=>",introduce)

    #基础低价
    def BasicsPrice(self,price):
        self.type("id=>",price)

    #周末低价
    def WeekendBottomPrice(self,price):
        self.type("id=>",price)

    #押金
    def Deposit(self,deposit):
        self.type("id=>",deposit)

    #退款规则
    def RefundPice(self):
        self.click("id=>")

    #入住时间
    def CheckInTime(self):
        self.click("id=>")

    #离店时间
    def DepartureTime(self):
        self.click("id=>")

    #接待时间
    def ReceptionStartTime(self):
        self.click("id=>")

    def ReceptionEndTime(self):
        self.click("id=>")

    #入住最少天数
    def CheckInLowDay(self):
        self.click("id=>")

    #入住最多天数
    def CheckInMostDay(self):
        self.click("id=>")

    #可住人数
    def CheckInPople(self,pople):
        self.type("id=>",pople)

    #是否接待外宾——是
    def ReceptionYes(self):
        self.click("id=>")

    #是否接待外宾——否
    def ReceptionNo(self):
        self.click("id=>")

    #是否允许吸烟——是
    def AllowSmokingYes(self):
        self.click("id=>")

    #是佛允许吸烟——否
    def AllowSomkingNo(self):
        self.click("id=>")

    #是否允许带宠物——是
    def AllowPetYes(self):
        self.click("id=>")

    #是否允许带宠物——否
    def AllowPetNo(self):
        self.click("id=>")

    #接待65以上老人——是
    def OldManYes(self):
        self.click("id=>")

    def OldManNo(self):
        self.click("id=>")

    #接待6岁以下小孩——是
    def ChildrenYes(self):
        self.click("id=>")

    #接待6岁以下小孩——否
    def ChildrenNo(self):
        self.click("id=>")

    #其他须知
    def OtherInstructions(self,instructions):
        self.type("id=>",instructions)

    #