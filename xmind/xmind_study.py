#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: xmind_study.py
@time: 2021/03/31
@remark：
"""
from xmindparser import xmind_to_dict
import json

xm = xmind_to_dict("团队学习-我的推课.xmind")[0]['topic']

# indent为显示json格式，ensure_ascii未显示为中文，不显示ASCII码
print(json.dumps(xm, indent=2, ensure_ascii=False))
