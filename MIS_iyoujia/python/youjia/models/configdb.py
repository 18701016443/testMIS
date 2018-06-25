#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/2/1 10:47
"""
import pymysql

def cord(phone):

    db = pymysql.connect(
        "172.16.10.51",
        "zhangjiaheng",
        "ykfamXiIB06mALRa",
        "youjia"
    )

    cursor = db.cursor()


    sql = "SELECT verificate_code FROM `user_session` WHERE mobile = %s ORDER BY create_time DESC LIMIT 1"%(phone)
    # print(sql)
    cursor.execute(sql)

    data = cursor.fetchone()
    db.close()
    # print(data)
    return data[0]

    # db.close()

