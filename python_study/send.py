#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: send.py
@time: 2020/07/16
@remark：
"""

from gril import has_gril
from show import send
import gril
print(f"send has_gril id is {id(has_gril)}")
has_gril = False
print(f"send has_gril id is {id(has_gril)}")
send()