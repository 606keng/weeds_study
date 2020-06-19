#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: login.py
@time: 2020/06/18 
"""
from carsir_test.easy_sell.api.login import Login
from carsir_test.easy_sell.test.demo.token import Token


def login():
    token = Login().get_carsir_token()
    setattr(Token,"token","token")