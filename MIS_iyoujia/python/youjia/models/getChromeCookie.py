#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/3/29 15:08
"""
import os
import sqlite3
import requests
import win32.win32crypt


def getcookiefromchrome(host='testmis.iyoujia.com'):
    cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql="select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu=conn.cursor()
        cookies={name:win32.win32crypt.CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        print(cookies["JSESSIONID"])
        return cookies


# url="http://testmis.iyoujia.com/#/login"
#
# httphead={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#
# r=requests.get(url,headers=httphead,cookies=getcookiefromchrome('testmis.iyoujia.com'),allow_redirects=1)

