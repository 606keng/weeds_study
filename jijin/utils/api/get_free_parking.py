#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: get_free_parking.py
@time: 2020/11/06
"""
import requests
from jsonpath import jsonpath

from utils.basepath import ConfigPath
from utils.db_operation import DbOperation
from utils.get_user_info import GetUserInfo
from utils.read_file import ReadFile


class GetFreeParking:
    host = "https://test.carsir.xin"
    headers = {
        "grp": "carsir_center",
        "Content-Type": "application/json; charset=utf-8",
    }
    mobile = GetUserInfo().get_check_user()
    passwd = GetUserInfo().get_center_passwd()

    def login_center(self):
        path = "/olympic/api-auth/admin/authorize/login"
        url = self.host + path
        data = {
            "username": f"{self.mobile}",
            "password": f"{self.passwd}"
        }
        req = requests.post(url, json=data, headers=self.headers).json()
        return req["data"]["accessToken"]

    def connect_db(self,database="olympic_admin"):
        db_info = ReadFile().read_json("db_config.json", ConfigPath)
        db = DbOperation(**db_info[database])
        return db

    def get_center_id(self):
        self.headers['Authorization'] = "Bearer " + self.login_center()
        path = f"/olympic/api-resource/admin/all/info/queryByMobile?mobile={self.mobile}"
        url = self.host + path
        req = requests.post(url, headers=self.headers).json()
        service_center_id = jsonpath(req,"$..serCenterId")
        db = self.connect_db()
        sql = f"select id from dht_sharing_center where service_center_id='{service_center_id[0]}';"
        center_id = db.select(sql)[0][0]
        return center_id

    def get_free_parking(self, ):
        path = f"/olympic/api-olympic-admin/dht/centercarposition/list/{self.get_center_id()}"
        url = self.host + path
        req = requests.post(url,headers=self.headers).json()
        return jsonpath(req,'$.data[?(@.parkingStatus == "CP_STATUS_FREE")].parkingPosition')[0]

    def sign_easy_shou_contrack(self,order_no):
        order_info = self.get_order_info(order_no)
        self.create_contract(**order_info)
        path = "/olympic/api-olympic-admin/contractController/backAdress"
        url = self.host + path
        self.headers["agentId"] = self.carsir_mobile
        self.headers['Authorization'] = "Bearer " + self.login_carsir()
        db = self.connect_db(database="carsir_agent")
        contract_id = \
        db.select(f"select contract_id from carsir_agent_contract where order_id='{order_info['order_id']}';")[0]
        print(contract_id)
        data = {"result_code": "3000", "contract_id": contract_id[0]}
        print(data)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"
        req = requests.post(url, data=data, headers=self.headers).json()
        return req

if __name__ == '__main__':
    contract = GetFreeParking()
    print(contract.get_free_parking())