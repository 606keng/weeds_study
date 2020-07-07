#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: faker_demo.py
@time: 2020/07/07 
"""
from faker import Faker
#locale="zh_CN"造出的数据为中文简体
fake = Faker(locale="zh_CN")
name = fake.name()
address = fake.address()
print(name,address)