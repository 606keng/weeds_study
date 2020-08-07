#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: lianxi.py
@time: 2020/06/18 
"""
from carsir_test.easy_sell.test.demo.login import login
from carsir_test.easy_sell.test.demo.token import Token


def test_login1():
    login()
    token = getattr(Token,"token")
    print(token)

def test_login2():
    login()
    token = getattr(Token,"token")
    print(token)

def test_login3():
    login()
    token = getattr(Token,"token")
    print(token)