#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/14 10:34
"""
from .base import Pyse

#导航栏定位，包括左侧大模块，模块内的小tab

class NavPage(Pyse):

    #基础服务
    def jichufuwu(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[2]/div")

    #加盟管理
    def LeagueManage(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[1]")

    #合作意向列表
    def CooperationList(self):
        self.click("xpath=>//*[@id='tab-apply_list']")

    #加盟申请列表
    def LeagueApplyList(self):
        self.click("xpath=>//*[@id='tab-join_list']")

    #确认加盟收款
    def SureReceivables(self):
        self.click("xpath=>//*[@id='tab-pay_list']")

    #合同列表
    def contract(self):
        self.click("xpath=>//*[@id='tab-contract_list']")

    #房源管理
    def RoomManage(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[2]")

    #房源管理列表
    def RoomManageList(self):
        self.click("xpath=>//*[@id='tab-fyList']")

    #房屋管理列表
    def HouseManage(self):
        self.click("xpath=>//*[@id='tab-fwList']")

    #房源资料修改审核
    def EidtRoom(self):
        self.click("xpath=>//*[@id='tab-fyChangeList']")

    #订单
    def OrderList(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[3]")

    #评论管理
    def Comment(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[4]")

    #配套服务
    def SupportingServices(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[3]/div")

    #软装管理
    def SoftOutfit(self):
        self.click("xpath=>//*[@id='app']/div/div/div[1]/ul/li[3]/ul/li[2]")