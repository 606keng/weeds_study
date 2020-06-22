#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: basepath.py
@time: 2020/06/19 
"""
import os

BasePath = os.path.dirname(os.path.dirname(__file__))
ConfigPath = os.path.join(BasePath,"config")
ApiPath = os.path.join(BasePath,"api")
DataPath = os.path.join(BasePath,"data")