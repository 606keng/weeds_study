#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 标准库.py
@time: 2020/07/12
@remark：涉及到os/time/datetime/math/urllib等第三方库的基本使用
"""

import os

# 创建目录
try:
    os.mkdir("testdir")
except:
    print("目录已存在")
# 查看当前目录有哪些文件
print(os.listdir("./"))
# 删除目录
os.removedirs("testdir")
# 输出当前文件的绝对路径
print(os.getcwd())

# 在当前目录下新建b目录，在该目录下新建test.txt文件，写入hello ,using os

if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt", "w")
    f.write("hello,using os")
    f.close()

import time

# 打印西方时间格式
print(time.asctime())
# 打印时间戳，时间戳为1970年1月1日0：0：0开始到现在的秒数
print(time.time())
# 时间戳转换为时间元组
print(time.localtime())
# 将时间戳转换为带格式的时间,输出结果：2020-07-12 23:47:07
print(time.strftime("%Y-%m-%d %H:%M:%S"))

"""获取两天前的时间"""
now_time = time.time()
two_day_before = now_time - 60 * 60 * 24 * 2
# time.localtime(two_day_before)将两天前的时间戳转换为时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day_before)))

"""获取两天后的时间"""
now_time = time.time()
two_day_after = now_time + 60 * 60 * 24 * 2
# time.localtime(two_day_before)将两天前的时间戳转换为时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day_after)))

import urllib.request

re = urllib.request.urlopen("http://www.baidu.com")
print(re.status)

import math

#返回大于等于参数x的最小整数
print(math.ceil(10.001))
#返回小于等于参数x的最大整数
print(math.floor(10.001))
#求平方根
print(math.sqrt(4))