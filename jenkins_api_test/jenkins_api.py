#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: jenkins_api.py
@time: 2020/06/27
"""
import configparser
import os


def get_jenkins_config(chose):
    config = configparser.ConfigParser()

    config.read(os.path.join(os.getcwd(),"jenkins.ini"))
    print(config)
    username = config.get(chose, "username")
    password = config.get(chose, "password")
    host = config.get(chose, "host")
    port = config.get(chose, "port")
    url = "http://" + host + ":" + port
    return url, username, password


if __name__ == '__main__':
    get_jenkins_config("jenkins")
