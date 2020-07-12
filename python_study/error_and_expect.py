#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: error_and_expect.py
@time: 2020/07/12
@remark：错误与异常
"""
try:
    num1 = int(input("请输入一个除数"))
    num2 = int(input("请输入一个被除数"))
    print(num1 / num2)
# 程序发生ZeroDivisionError异常，执行如下代码
except ZeroDivisionError:
    print("被除数不能为0")
# 程序发生ValueError异常，执行如下代码
except ValueError:
    print("除数或被除数不能为非数字字符")
# 程序未发生异常，执行如下代码
else:
    print("程序正常执行")
# 不管程序是否发生异常，执行如下代码
finally:
    print("程序已执行完毕")


# #自定义异常
# i = 10
# if i>5:
#     raise Exception("i不能大于5")

class MyException(Exception):
    def __init__(self):
        self.value = 4
raise MyException()