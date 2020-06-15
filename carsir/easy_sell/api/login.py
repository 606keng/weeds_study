import requests
import yaml

from request_study.api_ddatf.api.base_api import BaseApi


class Login(BaseApi):
    #获取token
    data = yaml.load(open(r"D:\work\auto\weeds_study\carsir\easy_sell\data\login.yaml"))
    def get_carsir_token(self):
        data={
            "method":"post",
            "url":"https://test.carsir.xin/olympic/api-olympic-auth/api/loginController/agentLogin",
            "json":self.data
        }
        return self.send_api(data)