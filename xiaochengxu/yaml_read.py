#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: yaml_read.py
@time: 2020/08/05 
"""
import json

import yaml

with open("xiaochengxu.yaml",encoding="utf-8") as f:
    a = yaml.safe_load(f)
# a = {'appPackage': 'com.consumer.carsir', 'appActivity': '.activity.StartPageActivity', 'platformName': 'android', 'deviceName': '79UNW19701000783', 'autoGrantPermissions': True, 'noReset': 'true', 'unicodeKeyBoard': True, 'resetKeyBoard': True, 'automationName': 'uiautomator1'}
print(json.dumps(a))