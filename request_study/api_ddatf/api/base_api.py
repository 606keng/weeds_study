from pprint import pprint

from jsonpath import jsonpath
import requests


class BaseApi:
    def send_api(self, req: dict):
        pprint(req)
        r=requests.request(**req)
        pprint(r.json())
        return requests.request(**req).json()
    @classmethod
    def jsonpath(self, json, expr):
        return jsonpath(json, expr)
