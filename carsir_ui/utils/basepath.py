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
PagePath = os.path.join(BasePath,"page")
DataPath = os.path.join(BasePath,"data")
StepsPath = os.path.join(BasePath,"steps")