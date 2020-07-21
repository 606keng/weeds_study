#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: return_fun_time.py
@time: 2020/07/21
@remark: 获取函数执行时间
"""
import time

#定义装饰器
def time_calc(fun):
    def wrap(*args,**kwargs):
        start_time = time.time()
        f = fun(*args,**kwargs)
        exec_time = time.time() - start_time
        print(exec_time)
        return f
    return wrap
@time_calc
def add(a,b):
    return a+b


print(add(23123123123123123123123123123123, 2123123123123123123123123123123))