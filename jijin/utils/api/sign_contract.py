#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: sign_contract.py
@time: 2020/11/04 
"""
import requests

from utils.basepath import ConfigPath
from utils.db_operation import DbOperation
from utils.get_user_info import GetUserInfo
from utils.read_file import ReadFile


class SignContract:
    host = "https://test.carsir.xin"
    headers = {
        "grp": "carsir_app",
        "Content-Type": "application/json; charset=utf-8",
    }
    carsir_mobile = GetUserInfo().get_carsir_mobile()

    def get_carsir_code(self):
        path = f"/olympic/api-resource/sms/customer/login/sendCode?mobile={self.carsir_mobile}"
        url = self.host + path
        req = requests.post(url, headers=self.headers).json()
        return req

    def login_carsir(self):
        self.get_carsir_code()
        path = "/olympic/api-auth/customer/authorize/login"
        url = self.host + path
        data = {
            "code": "111111",
            "mobile": f"{self.carsir_mobile}"
        }
        req = requests.post(url, json=data, headers=self.headers).json()
        return req["data"]["accessToken"]

    def connect_db(self,database="olympic_admin"):
        db_info = ReadFile().read_json("db_config.json", ConfigPath)
        db = DbOperation(**db_info[database])
        return db

    def get_order_info(self, order_no):
        db = self.connect_db()
        sql = f"select id ,CAST(finance_limit  AS CHAR) ,CAST(purchase_price  AS CHAR) ,CAST(minimum_price  AS CHAR)  from carsir_order where order_no='{order_no}';"
        info = db.select(sql)
        result = {"order_id": info[0][0],
                  "purchasePrice": info[0][2],
                  }
        return result

    def create_contract(self, order_id, purchasePrice):
        minimumPrice = float(purchasePrice)
        financeLimit = float(purchasePrice)*0.1
        path = "/olympic/api-olympic-admin/contractController/createEasySaleContract"
        url = self.host + path
        self.headers["agentId"] = self.carsir_mobile
        self.headers['Authorization'] = "Bearer " + self.login_carsir()
        data = {
            "carManageFee": "￥4.00\/天",
            "agentId": self.carsir_mobile,
            "orderId": order_id,
            "financeLimit": financeLimit,
            "minimumPrice": minimumPrice,
            "purchasePrice": purchasePrice
        }
        req = requests.post(url, json=data, headers=self.headers).json()
        return req

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
    contract = SignContract()
    print(contract.sign_easy_shou_contrack(order_no="QSS20201105164402570"))