#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: connect_devices.py
@time: 2020/08/26 
"""
import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.info)