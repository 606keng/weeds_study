#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: run.py
@time: 2021/02/04 
"""
import requests


def dispose_data(data):
    list_datas = data.split("&")
    dict_data = {}
    for list_data in list_datas:
        key = list_data.split("=")[0]
        value = list_data.split("=")[1]
        dict_data[key] = value
    return dict_data


def appoint():
    headers = {
        "Cookie": 'pin=jd_4a62da37672bc;wskey=AAJf-7LGAEAuUPmf0u05TAhbfpqbzcpMGPvAe5BowVbz6IxMVHhraVn-bMK4hnYdov5Jlt41acbsLsz3jngwGyNBgjpE-VhC;whwswswws=sFpbv8XfxScPujxl134jvo7CqUJJbY4x1K414GR4x1WX+P6Tp3ViodyjGufzyDqOTEN3Mm1ci9XftezFPxt+9sg==;unionwsws={"jmafinger":"sFpbv8XfxScPujxl134jvo7CqUJJbY4x1K414GR4x1WX+P6Tp3ViodyjGufzyDqOTEN3Mm1ci9XftezFPxt+9sg==","devicefinger":"eidI41920113Qjk5RjE3NjUtMTRDNS00MA==pvB9EWpbKPN6K707\/GfNYa20SQlPpTPzPyJEVkAfG7dTEtyIauULPk41+T4ovJSKR0NkMJ0AtR04Chc6"}'}
    headers["User-Agent"] = "JD4iPhone/167538 (iPhone; iOS 14.0.1; Scale/3.00)"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "adid=DB34281A-518C-427D-BD06-A6B277A632CD&area=27_2402_44320_56700&body=%7B%22isShowCode%22%3A%220%22%2C%22autoAddCart%22%3A%220%22%2C%22check%22%3A%220%22%2C%22skuId%22%3A%22100012043978%22%2C%22type%22%3A%221%22%2C%22appointMoreTimeFlag%22%3Afalse%2C%22mad%22%3A%220%22%7D&build=167538&client=apple&clientVersion=9.3.8&d_brand=apple&d_model=iPhone8%2C2&eid=eidI41920113Qjk5RjE3NjUtMTRDNS00MA%3D%3DpvB9EWpbKPN6K707/GfNYa20SQlPpTPzPyJEVkAfG7dTEtyIauULPk41%2BT4ovJSKR0NkMJ0AtR04Chc6&isBackground=N&joycious=250&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&openudid=1c1203f94732035054a63da17e16c362f52b57f0&osVersion=14.0.1&partner=apple&rfs=0000&scope=01&screen=1242%2A2208&sign=9a5e75b12ee552586f3d0987f78ea6ff&st=1612408588759&sv=122&uts=0f31TVRjBSuutMZFIdDzvxZ%2BFUwhkqknidExlBVi0WEDTqMR/73qfi0lhw1389iFv5Kl1suhiRE59k0Wa4joFDKBggFkJNn6Tkdo/GFiAGLMlOeepiFXIgcP2dHjsdF74Olt9n/Jnry1en58OmD4U/JXmxLvSDcXOXV64paNCryWBW0qM30LOwiRkEwG54EGBLJjNQeQ653pKFHQGnAkUg%3D%3D&uuid=hjudwgohxzVu96krv/T6Hg%3D%3D&wifiBssid=7ac3dcd31b5710dd929786dc0dbdc60a"
    url = "https://api.m.jd.com/client.action?functionId=appoint"
    re = requests.post(url=url, data=data, headers=headers)
    print(re.json())
# if __name__ == '__main__':
#     appoint()

def submit_order():
    headers = {}
    headers[
        "Cookie"] = 'seckillSid=; seckillSku=100012043978; unpl=V2_ZzNtbUJTFBV2CU5Te0xcUGIHFgoRVxYVdl9AUXlNWwZmA0AIclRCFnUUR1RnGlsUZwIZXkJcQhBFCEZkeRpdAmILE1xGZ3MdfWZFGXt3X2tnTl8QclRDJXQ4RlN7GVgNYwERWUZUShxzAE9Wfx1fNVcDFG1CVkIUdABGXXwbXQ1XMxNtQ2dCJT5mRxl7HlwFYwsWX0FTRxZ8AUBcchtYAWQzE21B%7CV2_ZzNtbUJfFBVwD0BVLkleUGIGG1gRURMdclpAXH0RDAxkUEVbclRCFnUUR1RnGV8UZgsZX0RcRxVFCEJkexhdBWEFElxCUHMlfGZFVn0ZXwxgCxEzQlZCezNWBREiShhNVwASbUNnQ0d1C0dWLBFZA2UAE19GVkcQJQ9EASsZWlFnBEBfRVQUEXZbQlIsGGw1bgIiWkVWQxJwCENVfBlsDGYLGl5GVkYJfQ5CXXgRbARXAiJcchYtFXQLR1N6GVhIZ1ESXkNVFB1wDkRXehtYBGMGQlpAAhMVc1xGUykbWwYwBxEORlEUFEUJdlQ%253d; mid=qc1QInCbhE5c5Bn3IMGAADxcXayWGh9W175JTUaH0uQ; seckill100012043978=03UhzYIJgcdmgEZDv98tJEKSszDKyclotJc53P6A6EGPlRDPGTR1OeFZBbXpv5yMDzfuAhrQQRWIa69/rWHbZteBak7tebTuE2thN7u+HvzGyG1PJ1XbOM84Cgu0UCwlf++dUlhieTINEsVdYkb1MwQCtNuTlfPdGF+L86xhDoNNO6mCvoTrgv8Ac8f3fAPwhSRjSMm1lwCWaMnk; pt_key=app_openAAJgCSPAADBV71lxHONIdzXNUWT85U0Om8te_x5_6PGkB2jCT2BOTmm_D_aGpAEq4cqNURkNjGs; pt_pin=jd_4a62da37672bc; pwdt_id=jd_4a62da37672bc; sid=64d84853f6f8f422918b71f3e279b70w; mba_muid=16103308498751070510287.86.1612410180671; mba_sid=86.33; __jd_ref_cls=MMySubscribe_BuyNow; __jda=121091540.16103308498751070510287.1610330849.1612404918.1612407658.74; __jdc=121091540; __jdv=121091540%7Ckong%7Ct_320649005_%7Cjingfen%7C15f120961d1d455fb1d12f743e6201cd%7C1611627666065; pre_seq=14; pre_session=1c1203f94732035054a63da17e16c362f52b57f0|170; 3AB9D23F7A4B3C9B=XJ7UPWI67RK5BOLCNAZ5DCZHZKJRVZ3SS5CK5DYVEYW5RUGSGAYMHIH5KMSPVJVRFQY6HEMZWJHO6FU526ZMOYU7B4; BATQW722QTLYVCRD={"tk":"jdd01K5Z2NXJTRK26CWX47R4JVNIIKAHE4JZREMK547PJLKQ37GBQV577DYT6SN2WJTUD6OWRH6KLPZOXPNDDEKYR6U3NPVXIDMSTRISFZEA01234567","t":1612173096034}; shshshfpb=xmK%20I5inTPbzfU1MIxvI18g%3D%3D; shshshfp=e6d6822b35ab7484c051d8c69c06e230; shshshfpa=2b242fab-8f09-9ddd-de1a-4eda2f08fa42-1611748628; qd_fs=1611803667909; qd_ls=1611803667909; qd_sq=2; qd_ts=1611873110523; qd_uid=KKGAADON-ORZHSOL2IGA9P546LIE9; __jdu=16103308498751070510287; visitkey=56219525787819703'
    headers["User-Agent"] = "JD4iPhone/167538 (iPhone; iOS 14.0.1; Scale/3.00)"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = 'num=2&addressId=3633649642&yuShou=true&isModifyAddress=false&name=%E8%B1%86%E7%AB%8B%E8%88%AA&provinceId=27&provinceName=%E9%99%95%E8%A5%BF&cityId=2402&cityName=%E5%92%B8%E9%98%B3%E5%B8%82&countyId=44320&countyName=%E7%A7%A6%E9%83%BD%E5%8C%BA&townId=56700&townName=%E9%99%88%E6%9D%A8%E5%AF%A8%E8%A1%97%E9%81%93&addressDetail=%E8%A5%BF%E5%92%B8%E5%A4%A7%E9%81%93%E6%B2%B3%E5%8D%97%E8%A1%97%E5%B0%8F%E5%8C%BA%E4%B8%9C%E5%8D%97100%E7%B1%B3%E4%B8%96%E7%BA%AA%E4%BC%98%E7%9B%98&mobile=187%2A%2A%2A%2A6614&mobileKey=008870c9bdb3bf46714aa797290cb74d&email=&invoiceTitle=4&invoiceCompanyName=&invoiceContent=1&invoiceTaxpayerNO=&invoiceEmail=&invoicePhone=187%2A%2A%2A%2A6614&invoicePhoneKey=008870c9bdb3bf46714aa797290cb74d&invoice=true&password=&codTimeType=3&paymentType=4&overseas=0&phone=&areaCode=86&token=d0af8449354639c5107d587fe31e1839'
    url = 'https://marathon.jd.com/seckillnew/orderService/submitOrder.action?skuId=100012043978'
    re = requests.post(url=url, data=data, headers=headers)
    print(re.text)


if __name__ == '__main__':
    while True:
        submit_order()
