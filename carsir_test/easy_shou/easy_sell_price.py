#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: easy_sell_price.py
@time: 2020/12/07 
"""


def get_easy_sell_price(pruchase_price, minimum_price, server_num, out_put_num, b_server_price, logistics_price):
    """

    :param pruchase_price: 评估师收购价
    :param minimum_price: 保留价
    :param server_num: 平台服务费系数
    :param out_put_num: 让价系数
    :param b_server_price: 小b佣金
    :param logistics_price: 物流费
    :return:
    """
    #   评估师收购价*卡先生服务费系数 ≥ 保留价 - 评估价 - 评估师收购价*让价系数
    if pruchase_price * server_num >= minimum_price - pruchase_price - pruchase_price * out_put_num:
        # 期望订单价下限 = 评估师收购价*（1+卡先生服务费系数）+ 小B服务费 + 物流费
        print("大于")

        return pruchase_price * (1 + server_num) + b_server_price + logistics_price
    else:
        # 期望订单价下限 = 全款供货价 - 评估师收购价*让价系数 + 小B服务费 + 物流费
        print("小于")
        return minimum_price + pruchase_price * server_num - pruchase_price * out_put_num + b_server_price + logistics_price


if __name__ == '__main__':
    print(get_easy_sell_price(40000, 50000, 0.04, 0.15, 2000, 0))
