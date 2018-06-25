#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/14 11:25
"""

from .base import Pyse
import datetime
from models import mydef
from time import sleep

#线索列表

class CooperationPage(Pyse):

    #去掉五家渠
    def wujiaqu(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/h3/label[2]/span[2]")

    #线索ID
    def CooperationID(self,id):
        self.type("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[1]/div[1]/div/input",id)

    #业主手机号
    def Phone(self,phone):
        self.clear("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[1]/div[3]/div/input")
        sleep(2)
        self.type("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[1]/div[3]/div/input",phone)

    #清除业主手机号
    # def clearPhone(self):
    #     self.move_to_element("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[1]/div[1]/div/input")
    #     self.click("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[1]/div[1]/div/span")

    #状态
    def State(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[2]/div[3]/div/div[1]/input")

    #待分配：2
    #待核验：3
    #通过：4
    #拒绝：5
    #已关单；6
    def ToBeAudited(self,i):
        self.click("xpath=>/html/body/div[2]/div[1]/div[1]/ul/li["+i+"]")

    #查询
    def Serch(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[1]/div/div[4]/button/span")

    #title跟进记录
    def TitleFollowUpRecord(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/h3/label/span[1]/span")

    # 跟进记录操作
    def FollowUpRecordBtn(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div/button[1]/span")

    #跟进记录弹窗
    def FollowUpRecordAlert(self):
        w = mydef.rad_word(5)
        self.type("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[4]/div/div[2]/div/textarea",w)

    #跟进记录弹窗确定按钮
    def PassBtn(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[4]/div/div[3]/div/button[2]/span")

    #跟进记录文案
    def textfollowuprecord(self):
        t = self.get_text("xpath=>/html/body/div[2]/p")
        return t



    #分配BD
    def DistributionBD(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr/td[13]/div/button[1]/span")

    #分配BD弹窗
    def DistributionBDAlert(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[3]/div/div[2]/div/div[1]/input")

    def selectBD(self,i):
        self.click("xpath=>/html/body/div[4]/div[1]/div[1]/ul/li["+i+"]/span")

    #分配BD弹窗确定按钮
    def DistributionBDAlertPass(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[3]/div/div[3]/div/button[2]/span")

    #分配BD弹窗取消按钮
    def DistributionBDAlertRefuse(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[3]/div/div[3]/div/button[1]/span")


    #通过
    def Pass(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div/button[2]/span")


    #二次确认
    def TwoPass(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[2]/span")

    #通过/拒绝提示文案
    def PromptText(self):
        text = self.get_text("xpath=>/html/body/div[4]/p")
        return text

    # 二次取消
    def TwoRefuse(self):
        self.click( "xpath=>/html/body/div[3]/div/div[3]/button[1]/span" )

    #拒绝
    def Refuse(self):
        self.click("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div/button[3]/span")

    #拒绝弹窗
    def RefuseAlert(self):
        # self.click("xpath=>/html/body/div[4]/div/div[2]/div[2]/div[1]/textarea")
        text = mydef.rad_word(10)
        self.type("xpath=>/html/body/div[3]/div/div[2]/div[2]/div[1]/textarea",text)




    #拒绝弹窗确定按钮
    def RefuseAlertPassbtn(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[2]/span")

    # 拒绝弹窗取消按钮
    def RefuseAlertRefusebtn(self):
        self.click( "xpath=>/html/body/div[3]/div/div[3]/button[1]/span" )



    #发起签约
    def StartLeague(self):
        self.open_new_window("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div/button[2]/span")


    #进入详情页面
    def OrderDetails(self):
        self.open_new_window("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")


    #详情页分配BD
    def DetailsBD(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[3]/button/span")

    #详情页分配BD弹窗选择BD
    def DetailsBDAlert(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/input")
        sleep(2)
        self.click("xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]/span")

    #详情页分配BD/修改BD弹窗确认按钮
    def DetailsBDAlertPass(self):
        self.click("xpath=>//*[@id='right-box']/div/div[5]/div/div[3]/div/button[2]/span")


    #详情页分配BD/修改BD弹窗取消按钮
    def DetailsBDAlertRefuse(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[4]/div/div[3]/div/button[1]/span")

    #详情页通过
    def DetailsPass(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[3]/button[1]/span")

    #详情页通过二次弹窗确认按钮/详情页拒绝弹窗确认按钮
    def DetailsPassAlert(self):
        self.click("xpath=>/html/body/div[2]/div/div[3]/button[2]/span")


    # 详情页通过二次弹窗取消按钮/详情页拒绝弹窗取消按钮
    def DetailsRefuseAlert(self):
        self.click( "xpath=>/html/body/div[2]/div/div[3]/button[1]/span" )


    #详情页拒绝
    def DtailsRefuse(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[3]/button[2]/span")


    #详情页拒绝弹窗
    def DtailsRefuseAlert(self,text):
        text = mydef.rad_word(10)
        self.type("xpath=>/html/body/div[2]/div/div[2]/div[2]/div[1]/textarea",text)

    # #详情页拒绝弹窗确认按钮
    # def DtailsRefuseAlertPassbtn(self):
    #     self.click("xpath=>/html/body/div[2]/div/div[3]/button[2]/span")

    #详情页修改BD
    def ReviseBD(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/button[3]/span")

    #修改BD弹窗选择BD
    def ReviseBDAlert(self):
        self.click("xpath=>//*[@id='right-box']/div/div[5]/div/div[2]/div/div[1]/input")
    def SelectBDAlert(self):
        self.click("xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[3]/span")


    #详情页发起加盟
    def OrderStartLeague(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[3]/button/span")

    #详情页查看加盟详情
    def CheckLeagueDtails(self):
        self.click("xpath=>//*[@id='app']/div/div/div[2]/div/div[3]/div[1]/button/span")

    #列表业主手机号，做比对用到
    def ListPhone(self):
        PT = self.get_text("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div")
        return PT

    #意向详情页BD名字
    def BDName(self):
        name = self.get_text("class=>BD_name")
        return name

    #列表状态
    def ListState(self):
        s = self.get_text("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div")
        return s

    #获取合作意向id
    def getID(self):
        id = self.get_text("xpath=>//*[@id='pane-apply_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")
        return id

