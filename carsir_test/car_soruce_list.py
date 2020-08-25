#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: car_soruce_list.py
@time: 2020/08/20 
"""
from _thread import start_new_thread
from time import sleep

import requests
import jsonpath


def get_car_source_list1(pageno="1"):
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


def get_car_source_list2(pageno="2"):
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


def get_my_car_source_list():
    data = {
        "carSourceStatus": "IN_STOCK",
        "pageNo": "1",
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


def in_detail():
    url = "https://test.carsir.xin/olympic/api-olympic-admin/easySell/carSource/carSourceDetails"
    data = {
        "shopId": "1272351631916408833",
        "carInfoId": "7121ff6060df4650a52cee3ce37ade9a"
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
        list3 = get_car_source_list1()
        in_detail()

        start_new_thread(get_my_car_source_list,())
        list1 = start_new_thread(get_car_source_list1, ())
        sleep(1)
        list2 = get_car_source_list2()
        print(f"list1; {list1}")
        print(f"list2; {list2}")
        # if list2[0] in list1:
        #     number += 1
        # if list1 != list3:
        #     number += 1
    print(number)


if __name__ == '__main__':
    run_list()
