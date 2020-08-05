#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: yaml_read.py
@time: 2020/08/05 
"""
import yaml

with open("carsir.yaml",encoding="utf-8") as f:
    print(yaml.safe_load(f))