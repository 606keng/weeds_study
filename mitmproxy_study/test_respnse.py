#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_respnse.py
@time: 2020/08/23
@remark：
"""
import json
from pprint import pprint


def response(flow):
    pprint(flow.response.content)
    data = json.loads(flow.response.content)
