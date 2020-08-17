#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: adb_shell.py
@time: 2020/08/17
@remark：
"""
import os

os.system('adb shell settings put secure default_input_method com.baidu.input/.ImeService')

