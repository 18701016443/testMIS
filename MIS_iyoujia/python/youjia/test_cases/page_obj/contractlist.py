#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/2/26 14:50
"""

from .base import Pyse

class ContractList(Pyse):
    """合同列表"""

    #五家渠
    def wujiaqu(self):
        self.click("xpath=>//*[@id='pane-contract_list']/div/div[2]/h3/label/span[2]")

    #查询条件——合同id
    def queryContractID(self,id):
        self.type("xpath=>//*[@id='pane-contract_list']/div/div[1]/div/div[1]/div[1]/div/input",id)

    #合同编号
    def ContractNumber(self):
        contractnumber = "ceshi"
        self.type("xpath=>//*[@id='pane-contract_list']/div/div[1]/div/div[3]/div[3]/div/input",contractnumber)

    #合同状态
        #已支付：12
    def ContractState(self):
        self.click("xpath=>//*[@id='pane-contract_list']/div/div[1]/div/div[2]/div[3]/div/div[1]/input")
    def SelectState(self,i):
        self.click("xpath=>/html/body/div[2]/div[1]/div[1]/ul/li["+i+"]/span")

    #是否归档
    def Filing(self):
        self.click("xpath=>//*[@id='pane-contract_list']/div/div[1]/div/div[4]/div/div/div[1]/input")
    def FilingState(self,statenum):
        # 已归档：2
        # 未归档：3
        self.click("xpath=>/html/body/div[3]/div[1]/div[1]/ul/li["+ statenum +"]/span")

    #查询
    def Search(self):
        self.click("xpath=>//*[@id='pane-contract_list']/div/div[1]/div/div[4]/button/span")

    #合同ID
    def ContractID(self):
        self.open_new_window("xpath=>//*[@id='pane-contract_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a/span")

    #获取合同ID
    def getContractID(self):
        id = self.get_text("xpath=>//*[@id='pane-contract_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span")
        return id

    #合同归档
    def File(self):
        self.click("xpath=>//*[@id='right-box']/div/div[3]/div")

    def PassBtn(self):
        self.click("xpath=>//*[@id='right-box']/div/div[10]/div/div[3]/span/button/span")

    #合同列表状态
    def listState(self):
        text = self.get_text("xpath=>//*[@id='pane-contract_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div")
        return text

    #获取房屋ID
    def get_HouseID(self):
        id = self.get_text("xpath=>//*[@id='pane-contract_list']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/span")
        return id

