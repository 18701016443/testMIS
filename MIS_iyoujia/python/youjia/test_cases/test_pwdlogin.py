#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/19 11:28
"""

from test_cases.page_obj import login_page
from  models import myunit
from time import sleep
import unittest,sys

class TestPwdLogin(myunit.MyTest):
    """账号密码登陆"""
    def test_pwdlogin(self):
        canshu = sys.argv[1]
        lp = login_page.LoginPage(self.driver,canshu)
        lp.open()
        sleep(1)
        lp.P_Phone(17601052158)
        sleep(1)
        lp.P_password("youjia123")
        sleep(1)
        lp.P_PictureCode("eeee")
        sleep(2)
        lp.P_LoginBtn()
        sleep(3)
        assert lp.LoginName() == "你好，张佳恒测试！欢迎使用Youjia MIS系统"

if __name__ == "__main__":
    unittest.main()