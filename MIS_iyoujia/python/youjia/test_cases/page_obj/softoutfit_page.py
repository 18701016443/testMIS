#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/1/26 10:38
"""
from .base import Pyse

class SoftOutfit(Pyse):
    """房屋软装管理列表"""

    #房屋ID
    def HouseID(self,id):
        self.type("xpath=>//*[@id='pane-decorationList']/div/div[1]/div/div[1]/div[1]/div/input",id)

    #查询
    def Search(self):
        self.click("xpath=>//*[@id='pane-decorationList']/div/div[1]/div/div[2]/button/span")

    #完成
    def PassBtn(self):
        self.click("xpath=>//*[@id='pane-decorationList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[12]/div/button[1]/span")

    #完成弹窗
    def TwoPassBtn(self):
        self.click("xpath=>/html/body/div[6]/div/div[3]/button[2]/span")

    #当前状态
    def NowState(self):
        text = self.get_text("xpath=>//*[@id='pane-decorationList']/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div")
        return text