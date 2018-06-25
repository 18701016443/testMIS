#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/19 11:28
"""

from .base import Pyse
from models import mydef
import datetime,time

#合同详情页

class Contract(Pyse):

    #a软装合同
    def SoftContract(self):
        self.click("xpath=>//*[@id='tab-softagreemt']")

    #编辑
    def Edit(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/div[1]")

    #提交审核
    def SubmissionOfAudit(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/div[1]")

    #确认提交审核
    def ConfirmBtn(self):
        self.click("xpath=>//*[@id='right-box']/div/div[5]/div/div[3]/span/button/span")

    #通过
    def Pass(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/div[1]")
    #二次确认
    def AlertPass(self):
        self.click("xpath=>//*[@id='right-box']/div/div[8]/div/div[3]/span/button/span")

    #合同审核——驳回
    def Refuse(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/div[2]")

    #合同审核——驳回合同理由
    def RefuseReason(self):
        Reason = mydef.rad_word(5)
        self.type("xpath=>//*[@id='right-box']/div/div[9]/div/div[2]/form/div[1]/div/div/textarea",Reason)

    #合同审核——驳回合同弹窗确认按钮
    def RefusePassBtn(self):
        self.click("xpath=>//*[@id='right-box']/div/div[9]/div/div[2]/form/div[2]/div/button/span")

    def RefuseSuccess(self):
        text = self.get_text("xpath=>/html/body/div[2]/p")
        return text

    #确认支付——主合同
    def PassPayment(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/div[1]")
    def PaymentAlert(self):
        self.click("xpath=>//*[@id='right-box']/div/div[10]/div/div[3]/span/button/span")

    #确认支付——软装合同
    def SoftContractPic(self):
        self.click("xpath=>//*[@id='right-box']/div/div[4]/div[1]")
    def SoftContractPicAlert(self):
        self.click("xpath=>//*[@id='right-box']/div/div[11]/div/div[3]/span/button/span")



    #合同编号
    def ContractID(self):
        id="chengzi"+mydef.rad_word(4)
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[1]/form/div/div/div/input",id)

    #纸质合同照片
    def ContractPhoto(self):
        self.click("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[2]/div/div[1]/div/button/span")

    #乙方：
    def FirstParty(self):
        name = "张佳恒测试"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[3]/div[1]/div/div[1]/div[1]/input",name)

    #身份证
    def IDcard(self):
        idcard = 341023199909071447
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[3]/div[1]/div/div[1]/div[2]/input",idcard)

    #代理人
    def Agent(self):
        agent = "zhangjiaheng"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[1]/div[1]/div[3]/input",agent)

    #代理人身份证
    def AgentIdCard(self):
        agentidcard = 341023199909071447
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[1]/div[1]/div[4]/input",agentidcard)

    #联系地址
    def Address(self):
        address = "张佳恒"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[2]/div[1]/div[1]/input",address)

    #联系电话
    def phone(self):
        phone = 18788889999
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[2]/div[1]/div[2]/input",phone)

    #电子邮箱
    def Email(self):
        email = "22@11.com"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[2]/div[1]/div[3]/input",email)

    #代理人联系地址
    def AgentAddress(self):
        address = "张佳恒测试"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[2]/div[2]/div[1]/input",address)

    #代理人电话
    def AgentPhone(self):
        agentphone = 17677773333
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[2]/div[2]/div[2]/input",agentphone)

    #代理人电子邮箱
    def AgentEmail(self):
        email = "qq@qq.com"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[2]/div[2]/div[2]/div[3]/input",email)

    #权属证明文件
    def Proof(self):
        text = self.get_text("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[1]/span[11]")
        return text

    #文件编号
    def DocumentNumber(self):
        document = "123123"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[1]/input[1]",document)

    #权属证书所登记的人为
    def ProofPeople(self):
        people = "ceshi"
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[1]/input[2]",people)

    #权属（租赁）期限
    def ServiceDataStart(self):
        # s = datetime.datetime.now().strftime("%Y-%m-%d")
        self.click("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[3]/div[2]/div[5]/div[1]/input")
        time.sleep(2)
        self.click("xpath=>/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/span")

    def ServiceDataEnd(self):
        # e = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # e = "2018-01-07"
        self.click("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[3]/div[2]/div[5]/div[2]/input")
        time.sleep(2)
        self.click("xpath=>/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[5]/div/span")

    #委托服务期限
    def DataStart(self):
        self.clear("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[2]/div[1]/input")
        s = datetime.datetime.now().strftime("%Y-%m-%d")
        s = int(s)
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[2]/div[1]/input",s)

    def DataEnd(self):
        self.clear("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[2]/div[2]/input")
        e = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        e = int(e)
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[3]/div[2]/div[2]/input",e)



    #合作费用与收益——品牌使用费
    def LanguePic(self):
        pic = mydef.rad_num(10,100)
        self.clear("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[1]/input[1]")
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[1]/input[1]",pic)

    #合作费用与收益——管理服务费
    def LangueBond(self,Bond):
        Bond = mydef.rad_num(10,99)
        self.clear("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[2]/input[1]")
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[2]/input[1]",Bond)

    #合作费用与收益——平台预订服务费
    def LangueSoftOutfit(self,softoutfit):
        softoutfit = mydef.rad_num(10,20)
        self.clear("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[3]/input[1]")
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[3]/input[1]",softoutfit)

    #合作费用与收益——筹建支持费
    def LangueDesignFee(self,designfee):
        designfee = mydef.rad_num(1,2000)
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[5]/input[1]",designfee)

    #合作费用与收益——业务收益
    def LangueCleaningFee(self):
        cleaningfee = mydef.rad_num(1,99)
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[7]/input",cleaningfee)


    #软装费用
    def SoftPic(self):
        pic = mydef.rad_num(1,1000)
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[3]/form/div[2]/div/div/input",pic)

    #软装押金
    def SoftDeposit(self):
        deposit = mydef.rad_num(1,1000)
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[1]/form/div[2]/div/div/input",deposit)

    #品牌升级相关费用
    def UpgradeCost(self):
        cost = mydef.rad_num(1,10)
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[7]/form/div[3]/div[1]/div/div/input",cost)

    #有家收款账户——银行卡
    def Card(self):
        self.click("xpath=>//*[@id='pane-softagreemt']/div/div[7]/form/div[2]/div/div/label[1]/span[1]/span")

    #有家收款账户——支付宝
    def zhifubao(self):
        self.click("xpath=>//*[@id='pane-softagreemt']/div/div[7]/form/div[2]/div/div/label[2]/span[1]/span")

    #床垫——租赁
    def BedLease(self):
        self.click("xpath=>//*[@id='pane-softagreemt']/div/div[5]/form/div/div/div/label[1]/span[1]/span")

    #床垫押金
    def BedLeaseNum(self,num):
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[5]/form/div[2]/div[2]/div/div/input",num)

    #每日总租金
    def BedLeasePic(self,pic):
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[5]/form/div[2]/div[1]/div/div/div/input",pic)

    #床垫——购买
    def BedBuy(self):
        self.click("xpath=>//*[@id='pane-softagreemt']/div/div[5]/form/div[1]/div/div/label[2]/span[1]/span")

    #床垫费用
    def BedFee(self,fee):
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[5]/form/div[2]/div/div/div/input",fee)

    #床垫——不使用床垫
    def BedNo(self):
        self.click("xpath=>//*[@id='pane-softagreemt']/div/div[5]/form/div[1]/div/div/label[3]/span[1]/span")

    #纸质合同
    def SoftContractUp(self):
        self.click("xpath=>//*[@id='pane-softagreemt']/div/div[9]/div/div[1]/div/button/span")

    #合同详情页状态
    def ContractState(self):
        text = self.get_text("xpath=>//*[@id='right-box']/div/p/span")
        return text

    #履约保证金_是
    def PerformanceBond(self):
        self.click("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[4]/div/div/div/div[2]/label/span[1]/span")

    #手动填写履约保证金
    def ManualPerformanceBond(self,pic):
        self.clear("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[4]/div/div[2]/p/span/input")
        self.type("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[4]/div[4]/div/div[4]/div/div[2]/p/span/input",pic)

    #运营升级费用
    def OperationUpgradeFee(self,fee):
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[1]/form/div/div/div/input",fee)

    #软装合同备注
    def ContractNotes(self,notes):
        self.type("xpath=>//*[@id='pane-softagreemt']/div/div[10]/div/textarea",notes)


    #预计交房时间
    def RoomTime(self):
        self.click("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[3]/div[2]/div[7]/div/input")
    def SelectDate(self):
        self.click("xpath=>/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[3]/div/span")

    #预计上线时间
    def OnlineDate(self):
        self.click("xpath=>//*[@id='pane-bsJoinagreemt']/div/div[3]/div[2]/div[8]/div/input")

    def SelectOnlineDate(self):
        self.click("xpath=>/html/body/div[6]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[6]/div/span")

