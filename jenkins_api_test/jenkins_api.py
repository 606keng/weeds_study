#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: jenkins_api.py
@time: 2020/06/27
"""
import configparser
import datetime
import logging
import os
import re

from jenkinsapi.jenkins import Jenkins

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

def get_jenkins_config(chose):
    config = configparser.ConfigParser()

    config.read(os.path.join(os.getcwd(),"jenkins_server.ini"))
    username = config.get(chose, "username")
    password = config.get(chose, "password")
    host = config.get(chose, "host")
    port = config.get(chose, "port")
    url = "http://" + host + ":" + port
    return url, username, password

class JenkinsDemo:
    def __init__(self,job_name, chose = "jenkins"):
        self.job_name = job_name
        config = get_jenkins_config(chose)
        #*config解包元组，useCrumb=True使用碎片
        self.jk = Jenkins(*config,useCrumb=True)

    def __get_job_from_keys(self):
        choose_list = []
        print(self.jk.keys())
        for my_job_name in self.jk.keys():
            if self.job_name in my_job_name:
                choose_list.append(my_job_name)
        return choose_list

    def __job_build(self,my_job_name):
        if self.jk.has_job(my_job_name):
            my_job = self.jk.get_job(my_job_name)
            #判断job是否在运行
            if not my_job.is_queued_or_running():
                try:
                    last_build = my_job.get_last_buildnumber()
                except:
                    last_build = 0
                build_num = last_build + 1
                #开始打包
                try:
                    self.jk.build_job(my_job_name)
                except Exception as e:
                    log.error(str(e))

                #循环判断Jenkins是否打包完成
                while True:
                    if not my_job.is_queued_or_running():
                        #获取最后一次打包信息
                        count_build = my_job.get_build(build_num)
                        #获取打包开始时间
                        start_time = count_build.get_timestamp() + datetime.timedelta(hours=8)
                        #获取打包日志
                        console_out = count_build.get_console()
                        #获取状态
                        status = count_build.get_status()
                        #获取变更内容
                        change = count_build.get_changeset_items()
                        p2 = re.compile(r".*ERROR.*")
                        err_list = p2.findall(console_out)
                        if status == "SUCCESS":
                            if len(change) > 0:
                                for data in change:
                                    for data in change:
                                        for file_list in data["affectedPaths"]:
                                            log.info("发起的" + my_job_name + "变更的类：" + file_list)
                                        log.info("发起的" + my_job_name + "变更的备注：" + data["msg"])
                                        log.info("发起的" + my_job_name + "变更提交人：" + data["author"]["fullName"])
                            else:
                                log.info("发起的" + my_job_name + "没有变更内容")
                            if len(err_list) > 0:
                                log.warning("构建的" + my_job_name + "构建状态为成功，但包含以下错误")
                                for error in err_list:
                                    log.error(error)
                        else:
                            if len(err_list) > 0:
                                log.warning("构建的" + my_job_name + "包含以下错误")
                                for error in err_list:
                                    log.error(error)
                        break
            else:
                log.warning("发起的" + my_job_name + "jenkins is running")
        else:
            log.warning("发起的" + my_job_name + "没有该服务")

    def run(self):
        my_job_name = self.__get_job_from_keys()
        print(my_job_name)
        if len(my_job_name) == 1:
            self.__job_build(my_job_name[0])
        elif len(my_job_name) == 0:
            log.error("输入的job名不正确")


if __name__ == '__main__':
    jk = JenkinsDemo("first_test")
    jk.run()