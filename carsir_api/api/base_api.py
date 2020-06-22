import logging
import os
from pprint import pprint
from time import time

import yaml
from jsonpath import jsonpath
import requests
from requests_toolbelt import MultipartEncoder

from carsir_api.utils.basepath import ConfigPath

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    level=logging.INFO)
class BaseApi:
    yaml.warnings({'YAMLLoadWarning': False})
    env = yaml.load(open(ConfigPath+r"/env.yaml","rb"))

    curret_url = env["environment"][env["default"]]
    def send_api(self, req: dict):
        # if req["headers"]["Content-Type"] == "application/x-www-form-urlencoded":
        #     pass

        req["url"] = req["url"].replace("carsir_host", self.curret_url)

        logging.info("请求参数：{}".format(str(req)))
        r = requests.request(**req)
        logging.info("响应结果：{}".format(r.json()))
        return r.json()

    def send_api_upload(self, req: dict):
        req["url"] = req["url"].replace("carsir_host", self.curret_url)
        req["data"] = MultipartEncoder(req["data"])
        req["headers"]["Content-Type"] = req["data"].content_type
        return requests.request(**req).json()

    @classmethod
    def jsonpath(self, json, expr):
        return jsonpath(json, expr)
