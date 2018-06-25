#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 10:41
"""
from random import choice
import string,random

#产生随机数
def rad_num(num1,num2):
    rad_num = random.randrange(num1,num2)
    rad_num = str(rad_num)
    return rad_num

#产生随机字母 + 数字
def rad_word(num):
    characters = string.ascii_letters + string.digits
    rad_word = "".join(choice(characters) for x in range(num))
    return rad_word

#产生随机字母
def rad_only_word(num):
    characters = string.ascii_letters
    rad_word = "".join(choice(characters) for x in range(num))
    return rad_word

if __name__ == "__main__":
    for i in range(1,5):
        # print(rad_word(15))
        l = rad_word(15)
        print(l.lower())

