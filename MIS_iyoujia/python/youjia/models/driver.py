#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/19 10:52
"""

from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ == "__main__":
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
