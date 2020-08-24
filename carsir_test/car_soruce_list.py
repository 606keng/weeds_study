#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: car_soruce_list.py
@time: 2020/08/20 
"""
from time import sleep

import requests
import jsonpath


def get_car_source_list(pageno):
    data = {
        "carSourceStatus": "OFF_SHELF",
        "pageNo": pageno,
        "pageSize": "10",
        "shopId": "1272351631916408833"
    }
    headers = {
        "token": "8cd2f95c0ff348a49aafed4cfe78b231",
        "agengId": "8142f6027ad344e49e9e7cc63f34dbef",
        "grp": "carsir_app",
        "Content-Type": "application/json; charset=utf-8"
    }
    url = "https://test.carsir.xin/olympic/api-olympic-admin/easySell/carSource/inStockCarSourceList"

    r = requests.post(json=data, headers=headers, url=url)
    return jsonpath.jsonpath(r.json(), "$.data.records.[::].carInfoId")


def in_detail():
    url = "https://test.carsir.xin/olympic/api-olympic-admin/easySell/carSource/carSourceDetails"
    data = {
        "shopId": "1272351631916408833",
        "carInfoId": "8eafffb7988a44de91f0ff711a0dae29"
    }
    headers = {
        "token": "8cd2f95c0ff348a49aafed4cfe78b231",
        "agengId": "8142f6027ad344e49e9e7cc63f34dbef",
        "grp": "carsir_app",
        "Content-Type": "application/json; charset=utf-8"
    }
    r = requests.post(json=data, headers=headers, url=url)


def run_list():
    number = 0
    for i in range(20):
        list3 = get_car_source_list("1")
        in_detail()
        list1 = get_car_source_list("1")
        sleep(1)
        list2 = get_car_source_list("2")
        print(f"list1; {list1}")
        print(f"list2; {list2}")
        if list2[0] in list1:
            number += 1
        if list1 != list3:
            number += 1
    print(number)


if __name__ == '__main__':
    run_list()
