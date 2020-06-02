import base64
import json

import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth

from request_study.test_suanfa import ApiRequest


class Test_Demo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.json())
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            'level': 1,
            'name': 'doulihang'
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        data = {
            'level': 1,
            'name': 'doulihang'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=data)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        json = {
            'level': 1,
            'name': 'doulihang'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=json)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        headers = {
            'level': "1",
            'name': 'doulihang'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', headers=headers)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["headers"]["Name"] == "doulihang"

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
        print("###################################",jsonpath(r.json(), "$..name"))
        assert jsonpath(r.json(), "$..name")[0] == "霍格沃兹测试学院公众号"

    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
        print("###################################",jsonpath(r.json(), "$..name"))
        assert_that(jsonpath(r.json(), "$..name")[0],equal_to("霍格沃兹测试学院公众号"))

    def test_cookie(self):
        url = "https://home.testing-studio.com/cookies"
        #通过header传递cookie
        header = {"Cookie":"doulihang"}
        r = requests.get(url=url,headers=header)
        print(r.request.headers)

        #通过cookies传递cookie
        cookie_data = {
            "goulihang":"gaoyujing"
        }
        r =requests.get(url=url,cookies=cookie_data)
        print(r.request.headers)

    def test_auth(self):
        url = "http://httpbin.testing-studio.com/basic-auth/banana/123"
        #通过auth访问接口
        auth = ("banana", "123")
        r = requests.get(url=url,auth=HTTPBasicAuth(*auth))
        print(r.text)

    def test_encode(self):
        """
        返回数据基于base64算法进行加密
        :return:
        """
        url = "http://127.0.0.1:9999/demo.txt"
        r = requests.get(url)
        #对返回数据进行解密,并转为json格式
        res = json.loads(base64.b64decode(r.content))
        print(res)

    def test_suanfa(self):
        req_data = {
            "method": "get",
            "url": "http://127.0.0.1:9999/demo.txt",
            "headers": None,
            "encoding": "base64"
        }
        #调用封装好的解密方法
        print(ApiRequest().send(req_data))
