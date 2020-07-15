#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_allure_severity.py
@time: 2020/07/15
@remark：用于标注用例的优先级
    BLOCKER = 'blocker'：中断缺陷--程序无响应，无法进行下一步操作
    CRITICAL = 'critical'：临界缺陷--功能点缺失
    NORMAL = 'normal'：一般缺陷--数值计算错误
    MINOR = 'minor'：次要缺陷--与UI图不符
    TRIVIAL = 'trivial'轻微缺陷--必填项无提示
如果想执行normal和minor级别的用例，执行命令如下：
pytest test_allure_severity.py --alluredir=result/7 --allure-severities normal,minor

如果类的等级是NORMAL，下面有两个方法，a没有等级，b等级为MINOR，
    只执行normal等级的用例时，只会执行a方法
    只执行minor等级的用例时，只执行b方法

"""
import allure


@allure.severity(allure.severity_level.NORMAL)
def test_severity_normal():
    print("NORMAL")

@allure.severity(allure.severity_level.BLOCKER)
def test_severity_blocker():
    print("BLOCKER")

@allure.severity(allure.severity_level.CRITICAL)
def test_severity_critical():
    print("CRITICAL")

@allure.severity(allure.severity_level.MINOR)
def test_severity_minor():
    print("MINOR")

@allure.severity(allure.severity_level.TRIVIAL)
def test_severity_trivial():
    print("TRIVIAL")

@allure.severity(allure.severity_level.NORMAL)
class TestNormal(object):
    def test_normal(self):
        print("normal")

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_trivial(self):
        print("TRIVIAL")