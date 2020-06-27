#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: jenkins_request.py
@time: 2020/06/27
"""
import requests


# url = "http://admin:123456@127.0.0.1:9090/job/test/build"
# r = requests.post(url)
# print(r.text)
#
def get_last_build_number():
    """
    获取Jenkins工程最后一次构建的数字。
    http://用户名:密码@host:port/job/job_name/lastBuild/buildNumber
    接口返回最近一次构建的数字
    :return:
    """
    url = "http://admin:123456@127.0.0.1:9090/job/test/lastBuild/buildNumber"
    r = requests.get(url)
    print(r.json())


def get_job_status():
    """
    获取jerkins指定工程第n次的构建状态
    http://用户名:密码@host:port/job/job_name/{buildNumber}/api/json
    :return:
    """
    url = "http://admin:123456@127.0.0.1:9090/job/test/2/api/json"
    r = requests.get(url)
    print(r.json())


if __name__ == '__main__':
    get_job_status()
