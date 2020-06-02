import requests

from request_study.api_ddatf.api.base_api import BaseApi


class WeWrok(BaseApi):
    corpid="wwcf22edd85b56740d"
    #获取token
    def get_token(self,secret):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid": self.corpid,
                "corpsecret": secret
            }
        }
        return self.send_api(data)