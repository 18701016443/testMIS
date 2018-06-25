#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/18 9:51
"""

from .base import Pyse
from models import mydef
from time import sleep
import os,datetime

#发起加盟——填写信息

class WriteLeague(Pyse):

    #业主姓名
    def YeZhuName(self):
        name = "张佳恒zhangjiaheng"
        self.type("xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div[1]/div/div[1]/div/div/input",name)

    #手机号
    def phone(self,phone):
        self.type("id=>",phone)


    #身份证号
    def IDCard(self,ID):
        self.type("id=>",ID)

    #开户名
    def BankName(self,bankname):
        self.type("id=>",bankname)

    #银行卡号
    def BankID(self,bankid):
        self.type("id=>",bankid)

    #开户银行
    def Bank(self):
        self.click("id=>")

    #开户支行_省份
    def BranchProvince(self):
        self.click("id=>")

    #开户支行_市
    def BranchCity(self):
        self.click("id=>")

    #开户支行_支行
    def BranchName(self):
        self.click("id=>")

    #身份证照片
    def UpIdCardPhoto(self):
        self.click("id=>")

    #品牌使用费
    def LeagueMoney(self,money):
        # money =mydef.rad_num(1,100)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[1]/div/div/div/div/input",money)

    #管理服务费
    def ServiceCharge(self,SC):
        # SC = mydef.rad_num(1,10)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[2]/div/div/div/div/input",SC)

    #有家分成比例
    def Proportions(self,proportions):
        # proportions = mydef.rad_num(1,100)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[3]/div/div/div/div/input",proportions)

    #委托服务期限
    def WTServicePeriodStart(self):
        s = datetime.datetime.now().strftime("%Y-%m-%d")
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[4]/div/div/div/div[1]/input",s)

    def WTServicePeriodEnd(self):
        e = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[4]/div/div/div/div[2]/input",e)

    #业主预期月租金
    def ExpectRent(self):
        nub = mydef.rad_num(1,999)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[5]/div[1]/div/div/div/input",nub)

    #是否加盟者本人房产
    def LeagueRoomYes(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[2]/div/div/label[1]/span[1]/span")

    def LeagueRoomNo(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[2]/div/div/label[2]/span[1]/span")

    #证件类型_房产证
    def DocumentTypePOC(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[3]/div[1]/div/div/label[1]/span[1]/span")


    #证件类型_租房合同
    def Lease(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[3]/div[1]/div/div/label[2]/span[1]/span")

    #证件照片
    def DocumentTypePhoto(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[3]/div[2]/div/div/div/div/button/span")

    def AutoIt(self):
        os.system( "D:/python/youjia/data/up.exe" )

    #授权书
    def CertificateOfAuthorization(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[3]/div[3]/div/div/label[1]/span[1]/span")

    #承诺书
    def LetterOfCommitment(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[3]/div[3]/div/div/label[2]/span[1]/span")

    #上传承诺书
    def UpLetterOfCommitment(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[4]/div/div/div[3]/div[4]/div/div/div/div/button/span")

    #房源类型
    def RoomType(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[2]/div/div/div/div[1]/input")
    def selectType(self):
        self.click("xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]/span")

    #户型_室
    def RoomNum(self):
        num = mydef.rad_num(1,5)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[3]/div/div/div[1]/div/input",num)

    #户型_厅
    def Parlor(self):
        parlor = mydef.rad_num(1,5)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[3]/div/div/div[2]/div/input",parlor)

    #户型_卫
    def Toilet(self):
        toilet = mydef.rad_num(1,5)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[3]/div/div/div[3]/div/input",toilet)

    # 户型_厨房
    def Kitchen(self):
        kitchen = mydef.rad_num(1,5)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[3]/div/div/div[4]/div/input",kitchen)

    #户型_阳台
    def Balcony(self):
        balcony = mydef.rad_num(1,5)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[3]/div/div/div[5]/div/input",balcony)

    #面积
    def Area(self):
        area = mydef.rad_num(1,200)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[4]/div/div/div/div/input",area)
    #房租
    def fangzu(self):
        pic = mydef.rad_num(1,100)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[5]/div/div/div/div/input",pic)

    #楼层
    def Floor(self):
        floor = mydef.rad_num(1,10)
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[6]/div/div/div/div/input",floor)

    # 是否有电梯
    def Elevator(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[6]/div/div/div/span")

    #详细地址
    def DetailedAddress(self):
        address = "测试"
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[10]/div/div[1]/div/div/input",address)


    #小区
    def Residentialquarters(self):
        # RQ = "爱情公寓"
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[10]/div/div[2]/div/div[1]/input")
        sleep(1)
        self.click("xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]/span")


    #门牌号
    def DoorNumbe(self):
        doornum = "1楼(测试)"
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[5]/div/div/div[10]/div/div[3]/div/input",doornum)

    #地图小锚点
    def maodian(self):
        #xpath和link_text都定位不到，因此采用css定位
        self.click("css=>.BMap_noprint,.anchorTL")

    #提交审核
    def Submit(self):
        self.click("xpath=>//*[@id='right-box']/div/div[2]/div[2]/button/span")

    #提交成功获取成功文案
    def SuccessText(self):
        text = self.get_text("xpath=>/html/body/div[2]/p")
        return text

    #预期短租月收益
    def ExpectProfit(self):
        pic = 10
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[5]/div[1]/div/div/div/input",pic)

    #长租月租金
    def LongMonthlyRent(self):
        p = 100
        self.type("xpath=>//*[@id='right-box']/div/div[2]/div[1]/form/div[3]/div/div/div[6]/div[1]/div/div/div/input",p)

