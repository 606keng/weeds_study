#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: study_rsa.py
@time: 2020/07/29 
"""
import base64
import json

import requests
import rsa

#
# def test_save_ras():
#     pubkey, privkey = rsa.newkeys(1024)
#
#     pub = pubkey.save_pkcs1()
#     pri = privkey.save_pkcs1("PEM")
#     with open("pubkey.pem", "wb") as f, open("privkey.pem", "wb") as f1:
#         f.write(pub)
#         f1.write(pri)
#
#
# def test_open_ras():
#     with open("pubkey.pem", "rb") as f, open("privkey.pem", "rb") as f1:
#         pub = f.read()
#         pri = f1.read()
#         pubkey = rsa.PublicKey.load_pkcs1(pub)
#         privkey = rsa.PrivateKey.load_pkcs1(pri)
#     message = '10000'
#     info = rsa.encrypt(message.encode("utf-8"), pubkey)
#     msg = rsa.decrypt(info, privkey)
#     print(msg.decode("utf-8"))
#     print(info)
#
#
# def with_ras(mes):
#     pubkey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCBjh/vEXjGKhvne8ntqYCHgK/Gvi73tillKZmttAb2CFWDQYUTLew/HxpPjpn/LhA2MMCMi+puHwa2nhU+teicgBTFSYrnB3dRkgTJ+gjk+lVRnrSMdPJxEV6w/tBTD2uJcmyHB5t7WFoLhdGYgaOgyg7P9CZ7JpmTC30Cmg16wwIDAQAB"
#     # with open("pubkey.pem", "rb") as f:
#     #     pub = f.read()
#     #     pubkey = rsa.PublicKey.load_pkcs1(pub)
#     key_bytes = base64.b64decode(pubkey)
#
#     info = rsa.encrypt(mes.encode("utf-8"), pubkey)
#     return base64.b64encode(info)
import base64

from Crypto.Hash import MD5
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

import rsa
import base64
from Crypto.PublicKey import RSA


def zfillStrToBin(s):
    # b = bytes(s.encode())
    for i in range(128 - len(s)):
        s += b'\0'
    print(len(s))
    return s


class RsaNopadding:

    def __init__(self, key):
        self.pubkey = RSA.importKey(base64.b64decode(key))

    def encrypt(self, message):
        kLen = rsa.common.byte_size(self.pubkey.n)
        print(type(message))
        msg = zfillStrToBin(message)
        _b = rsa.transform.bytes2int(msg)
        _i = rsa.core.encrypt_int(_b, self.pubkey.e, self.pubkey.n)
        result = rsa.transform.int2bytes(_i, kLen)
        return result.hex().upper()


def get_encrypt_data(params):
    """分段加密"""
    print(params)
    params = json.dumps(params)
    params = params.encode("utf-8")
    length = len(params)
    default_length = 117
    if length < default_length:
        return encrypt_data(params)
    offset = 0
    params_lst = []
    while length - offset > 0:
        if length - offset > default_length:
            params_lst.append(encrypt_data(params[offset:offset+default_length]))
        else:
            params_lst.append(encrypt_data(params[offset:]))
        offset += default_length
    res = "".join(params_lst)
    print(res)
    return base64.b64encode(res)


def encrypt_data(params):
    """使用公钥对数据加密"""
    key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCBjh/vEXjGKhvne8ntqYCHgK/Gvi73tillKZmttAb2CFWDQYUTLew/HxpPjpn/LhA2MMCMi+puHwa2nhU+teicgBTFSYrnB3dRkgTJ+gjk+lVRnrSMdPJxEV6w/tBTD2uJcmyHB5t7WFoLhdGYgaOgyg7P9CZ7JpmTC30Cmg16wwIDAQAB"
    # cipher = RsaNopadding(key).encrypt(params)
    rsakey = RSA.importKey(base64.b64decode(key))
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    print(type(cipher))
    text = cipher.encrypt(params)
    return base64.b64encode(text)

def apply_cash_balance():
    url = "https://test.carsir.xin/business/AgentApplyCashoutController/applyCashBalance"
    headers = {
        "token":"0bef0b1ba02144529df44ca7be7d8778",
        "agentId":"8142f6027ad344e49e9e7cc63f34dbef",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = {
        "transaPasswd":"921016",
        "agentId":"8142f6027ad344e49e9e7cc63f34dbef",
        "card_no_type":"2",
        "pay":"200"
    }
    data["transaPasswd"] = get_encrypt_data(data["transaPasswd"])
    data["agentId"] = get_encrypt_data(data["agentId"])
    data["pay"] = get_encrypt_data(data["pay"])
    # data["transaPasswd"] = str(get_encrypt_data(data["transaPasswd"]))
    # data["agentId"] = str(get_encrypt_data(data["agentId"]))
    # data["pay"] = str(get_encrypt_data(data["pay"]))
    r = requests.post(url=url,data=data,headers=headers)
    return r.json()



if __name__ == '__main__':
    print(apply_cash_balance())


"""
平台收益：
    轻松配：
            供货价 - 保留价 - 轻松卖服务费
    轻松售：
            供货价 - 保留价 - 轻松卖服务费
"""