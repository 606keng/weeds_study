from pprint import pprint
from jsonpath import jsonpath
import requests
from requests_toolbelt import MultipartEncoder


class BaseApi:
    def send_api(self, req: dict):
        if req["headers"]["Content-Type"] == "application/x-www-form-urlencoded":
            pass
        return requests.request(**req).json()

    def send_api_upload(self, req: dict):
        req["data"] = MultipartEncoder(req["data"])
        req["headers"]["Content-Type"] = req["data"].content_type
        return requests.request(**req).json()

    @classmethod
    def jsonpath(self, json, expr):
        return jsonpath(json, expr)
