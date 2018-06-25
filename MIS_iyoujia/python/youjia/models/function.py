#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/19 10:55
"""
from selenium import webdriver
import os

#截图函数
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace("\\","/")
    base = base_dir.split("/test_case")[0]
    file_path = base + "/report/images/" + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_img(driver,"baidu.png")
    driver.quit()
