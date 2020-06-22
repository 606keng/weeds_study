import os

import requests
import yaml

from carsir_api.api.base_api import BaseApi


class Login(BaseApi):
    module_path = os.path.dirname(__file__)
    #获取token
    data = yaml.load(open(module_path + "\login.yaml"))
    def get_carsir_token(self):
        print(self.data)
        data={
            "method":"post",
            "url":"https://carsir_host/olympic/api-olympic-auth/api/loginController/agentLogin",
            "json":self.data
        }
        return self.send_api(data)
if __name__ == '__main__':
    print(Login().get_carsir_token())