import requests
import yaml

from carsir_test.easy_sell.api.base_api import BaseApi


class Login(BaseApi):
    #获取token
    data = yaml.load(open(r"/carsir_test\easy_sell\data\login.yaml"))
    def get_carsir_token(self):
        print(self.data)
        data={
            "method":"post",
            "url":"https://carsir_host/olympic/api-olympic-auth/api/loginController/agentLogin",
            "json":self.data
        }
        return self.send_api(data)
if __name__ == '__main__':
    Login().get_carsir_token()