#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/1/26 10:09
"""
from .base import Pyse

class HouseManagePage(Pyse):

    """房屋管理"""

    #五家渠
    def wujiaqu(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/h3/label/span[1]/span")

    #业主账号
    def OwnerPhone(self):
        phone = 18701016443
        self.type("xpath=>//*[@id='pane-fwList']/div/div[1]/div/div[1]/div[1]/div/input",phone)

    #查询条件——房屋ID
    def input_HouseID(self,id):
        self.type("xpath=>//*[@id='pane-fwList']/div/div[1]/div/div[2]/div[3]/div/input",id)

    #列表房屋ID
    def list_HouseID(self):
        self.open_new_window("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")

    #房屋状态
    def HouseState(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[1]/div/div[2]/div[2]/div/div[1]/input")

    #房屋待签约：2
    #改装准备中：4
    #待合并处理：5
    #待上线：6
    #已上线：7
    #已下线：8
    def SelectState(self,i):
        self.click("xpath=>/html/body/div[2]/div[1]/div[1]/ul/li["+ i +"]/span")

    #查询
    def Seach(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[1]/div/div[2]/button/span")

    #获取房屋ID
    def HouseID(self):
        ID = self.get_text("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")
        return ID

    #完成保洁
    def FinishCleaning(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[15]/div/button[2]/span")


    #完成保洁弹窗——确认按钮
    def PassBtn(self):
        self.click("xpath=>/html/body/div[2]/div/div[3]/button[2]/span")


    #保洁状态
    def CleanState(self):
        text = self.get_text("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div")
        return text

    #获取房源ID
    def get_RoomID(self):
        id = self.get_text("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div")
        return id


    #编辑基础信息
    def EditHouse(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[2]/div[2]/button/span")

    #房屋标题
    def HouseTitle(self,title):
        self.type("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[3]/div/div/form/div[1]/div/div/div/div/input",title)

    #房屋简称
    def HouseNickAbbreviation(self,Abbreviation):
        self.type("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[3]/div/div/form/div[2]/div/div/div/div/input",Abbreviation)

    #电器设备——淋浴
    def Shower(self,shower):
        self.type("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[6]/div/div/form/div[2]/div[1]/div/div/div/div/input",shower)

    #床——单人床（2*0.8）
    def SingleBed(self,bed):
        self.type("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[6]/div/div/form/div[4]/div[1]/div/div/div/div/input",bed)

    #房屋照片
    #封面
    def Cover(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[7]/div/div/div[1]/div/div/i")

    #客厅
    def Parlour(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[7]/div/div/div[2]/div/div/div/button/span")

    #卧室
    def Bedroom(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[7]/div/div/div[3]/div/div/div/button/span")

    #厨房
    def Kitchen(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[7]/div/div/div[4]/div/div/div/button/span")

    #卫浴
    def Bathroom(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[7]/div/div/div[5]/div/div/div/button/span")

    #其他
    def Other(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[1]/div[7]/div/div/div[6]/div/div/div/button/span")

    #提交基础信息
    def submitBtn(self):
        self.click("xpath=>//*[@id='pane-bsJoinfwDetail']/div/div[2]/div[2]/button/span")

    #房屋列表——房屋状态
    def ListHouseState(self):
        text = self.get_text("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr/td[9]/div/span")
        return text

    #预约交接
    def Appointment(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[15]/div/button[2]/span")

    #请录入与业主预约的交接时间
    def AppointmentDate(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[6]/div/div[2]/div[2]/div[1]/div/input")
    def ThisMoment(self):
        self.click("xpath=>/html/body/div[4]/div[2]/button[1]/span")

    #备注信息
    def Remark(self):
        msg = "zhangjiaheng测试"
        self.type("xpath=>//*[@id='pane-fwList']/div/div[2]/div[6]/div/div[2]/div[2]/div[2]/textarea",msg)

    #确定
    def Determine(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[6]/div/div[3]/div/button[2]/span")


    #完成交接
    def CompleteAppointment(self):
        self.open_new_window("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[15]/div/button[3]/span")


    #上传图片
    def AppointmentPicture(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/div[3]/div/div[1]/div/button/span")

    #预计筹建完成日
    def CompletionDate(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[1]/div/div/div[3]/div/input")
    def CompletionDateNow(self):
        self.click("xpath=>/html/body/div[2]/div[2]/button[1]/span")

    #保存
    def AppointmentSave(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[2]/div/button/span")


    #通知验收
    def NoticeCheck(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[15]/div/button[3]/span")

    #请输入管家可以进行房屋验收的日期
    def CheckDate(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[8]/div/div[2]/div/div[1]/div/input")
    #选择时间
    # def SelectTime(self):
    #     self.click("xpath=>/html/body/div[3]/div[2]/button[1]/span")

    #确定
    def NoticeCheckBtn(self):
        self.click("xpath=>//*[@id='pane-fwList']/div/div[2]/div[8]/div/div[3]/div/button[2]/span")

    #完成验收
    def CompletionOfAcceptance(self):
        self.open_new_window("xpath=>//*[@id='pane-fwList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[15]/div/button[2]/span")
    def CompletionOfAcceptanceSave(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[2]/div/button/span")

    #弹窗——编辑房屋
    def AlertEditHouse(self):
        self.open_new_window("xpath=>//*[@id='right-box']/div/div[3]/div/div[3]/div/button[2]/span")









