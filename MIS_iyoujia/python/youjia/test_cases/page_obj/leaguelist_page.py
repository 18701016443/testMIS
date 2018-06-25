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
from time import sleep
import datetime

#加盟列表

class LeagueList(Pyse):

    # 五家渠
    def wujiaqu(self):
        self.click("xpath=>//*[@id='pane-join_list']/div/div[2]/h3/label/span[2]")

    #查询条件——加盟ID
    def InputLeagueID(self,id):
        self.type("xpath=>//*[@id='pane-join_list']/div/div[1]/div/div[1]/div[1]/div/input",id)

    #业主手机号
    def Phone(self,phone):
        # phone = 18701016443
        self.type("xpath=>//*[@id='pane-join_list']/div/div[1]/div/div[3]/div/div/input",phone)

    #检索条件的——加盟状态
    def State(self):
        self.click("xpath=>//*[@id='pane-join_list']/div/div[1]/div/div[2]/div[1]/div/div[1]/input")
    #待审核：2
    #待验收确认：3
    #审核不通过：4
    #合同编辑中：5
    #拒绝收房：6
    #待合同审核：7
    #待签约：8
    #合同不通过：9
    #已签约待支付：10
    #加盟完成：11
    #取消加盟：12
    #业主违约：13
    def SelectState(self,i):
        self.click("xpath=>/html/body/div[2]/div[1]/div[1]/ul/li["+i+"]/span")
    def TwoSelectState(self,i):
        self.click("xpath=>/html/body/div[3]/div[1]/div[1]/ul/li["+i+"]/span")

    # #创建时间开始
    # def CreateStart(self):
    #     start = datetime.datetime.now().strftime("%Y-%m-%d")
    #     self.type("id=>",start)
    #
    # def CreateEnd(self):
    #     end = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    #     self.type("id=>",end)

    #获取加盟ID
    def LeagueID(self):
        id = self.get_text("xpath=>//*[@id='pane-join_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")
        return id


    #加盟状态
    def LeagueState(self):
        t = self.get_text("xpath=>//*[@id='pane-join_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div")
        return t

    #房源所在区域_市
    def RoomAreaCity(self):
        self.click("id=>")

    def RoomAreaQu(self):
        self.click("id=>")

    #站点
    def Site(self):
        self.click("id=>")

    #搜索
    def Serach(self):
        self.click("xpath=>//*[@id='pane-join_list']/div/div[1]/div/div[3]/button/span")

    #加盟详情页
    def LeagueDetails(self):
        self.open_new_window("xpath=>//*[@id='pane-join_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")

    #查看合同
    def CheckContract(self):
        self.open_new_window("xpath=>//*[@id='right-box']/div/div[2]/div/div[10]/button/span")

    #编辑合同
    def EidtContract(self):
        self.open_new_window("xpath=>//*[@id='pane-join_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button/span")



    #审核合同
    def AuditContract(self):
        self.open_new_window("xpath=>//*[@id='pane-join_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button/span")


    #通过
    def Pass(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[2]/button/span")

    #驳回
    def Rufuse(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[3]/button/span")

    #修改
    def Revise(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[4]/button/span")

    #提交审核
    def Submit(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[4]/button/span")

    #取消加盟
    def CancelLeague(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[5]/button/span")

    #线下房管编辑
    def Edit(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[6]/button/span")

    # 完成验收交接
    def FinishJoin(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[6]/button/span")

    #验收交接确定按钮
    def FinishJoinAlertPassBtn(self):
        self.click("xpath=>/html/body/div[5]/div/div[3]/button[2]/span")

    #验收交接取消按钮
    def FinishJoinAlertCancelBtn(self):
        self.click("xpath=>/html/body/div[5]/div/div[3]/button[1]/span")

    #拒绝收房
    def RefuseJoinRoom(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[7]/button/span")

    #业主违约
    def DefaultOfEmployer(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div/div[11]/button/span")

    #分配站点弹窗
    def SiteAlert(self):
        self.click("xpath=>//*[@id='right-box']/div/div[3]/div/div[2]/div/div[1]/input")
    def selectsite(self,i):
        self.click("xpath=>/html/body/div[4]/div[1]/div[1]/ul/li["+i+"]/span")

    #分配站点弹窗确定按钮
    def ConfirmBtn(self):
        self.click("xpath=>//*[@id='right-box']/div/div[3]/div/div[3]/div/button[2]/span")

    #分配站点弹窗取消按钮
    def CancelBtn(self):
        self.click("xpath=>//*[@id='right-box']/div/div[3]/div/div[3]/div/button[1]/span")


    #加盟驳回弹窗B
    def AlertB(self):
        reason = mydef.rad_word(10)
        self.type("xpath=>/html/body/div[3]/div/div[2]/div[2]/div[1]/input",reason)


    #加盟驳回弹窗B确定按钮
    def AlertB_PassBtn(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[2]/span")

    #加盟驳回弹窗B取消按钮
    def AlertB_CancelBtn(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[1]/span")

    #取消加盟/业主违约弹窗C
    def AlertC(self):
        reason = mydef.rad_word(10)
        self.type("xpath=>/html/body/div[3]/div/div[2]/div[2]/div[1]/input",reason)

    #取消加盟/业主违约弹窗C确定按钮
    def AlertC_PassBtn(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[2]/span")

    #取消加盟/业主违约弹窗C取消按钮
    def AlertC_CancelBtn(self):
        self.click("xpath=>/html/body/div[3]/div/div[3]/button[1]/span")


    # #水电气交割
    # #水表
    # def Water(self):
    #     n = mydef.rad_num(1,100)
    #     self.type("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[7]/div/div/form[2]/div[2]/div[1]/div/div/div/input",n)
    #
    # #电表
    # def Electric(self):
    #     n = mydef.rad_num(1,100)
    #     self.type("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[7]/div/div/form[2]/div[2]/div[2]/div/div/div/input",n)
    #
    # #燃气
    # def Gas(self):
    #     n = mydef.rad_num(1,100)
    #     self.type("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[7]/div/div/form[2]/div[2]/div[3]/div/div/div/input",n)

    #房屋设施及内部状况验收单（作为合同附件）
    def AcceptanceCheck(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[7]/div/div/form/div[2]/div/div/div/div/div/button/span")

    #备注
    def OtherRemarks(self):
        m = mydef.rad_word(5)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[7]/div/div/form/div[4]/div/div/textarea",m)

    #软装方案照片
    def SoftPhoto(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[8]/div/div/form/div[2]/div/div/div/div/div/button/span")

    #软装公司
    def SoftCompany(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[8]/div/div/form/div[3]/div/div/div/div[1]/input")
    def ClickCompany(self):
        self.click("css=>body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(16)")

    #设计师
    def Designer(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[8]/div/div/form/div[4]/div/div/div/div[1]/input")
    def ClickDesigner(self):
        self.click("css=>body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)")

    #软装预算
    def Budget(self):
        n = mydef.rad_num(100,999)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/form/div/div[8]/div/div/form/div[7]/div/div/div/div/input",n)



