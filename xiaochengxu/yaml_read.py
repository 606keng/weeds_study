#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: yaml_read.py
@time: 2020/08/05 
"""
import json

import yaml

def read_yaml():
    with open("xiaochengxu.yaml",encoding="utf-8") as f:
        a = yaml.safe_load(f)
    # a = {'appPackage': 'com.consumer.carsir', 'appActivity': '.activity.StartPageActivity', 'platformName': 'android', 'deviceName': '79UNW19701000783', 'autoGrantPermissions': True, 'noReset': 'true', 'unicodeKeyBoard': True, 'resetKeyBoard': True, 'automationName': 'uiautomator1'}
    print(json.dumps(a))

def write_yaml():
    caps = {
            'platformName': 'Android',
            'fastReset': 'false',
            'noReset': True,
            # 'platformVersion': '9',
            'deviceName': '79UNW19701000783',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'fullReset': 'false',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:appbrand0'
            },
            "chromedriverExecutable": "/Users/doulihang/work/project/weeds_study/xiaochengxu/chromedriver",
            "automationName":"UiAutomator2"
        }
    with open('config.yaml',"w") as f:
        yaml.safe_dump(caps,f)

if __name__ == '__main__':
    write_yaml()