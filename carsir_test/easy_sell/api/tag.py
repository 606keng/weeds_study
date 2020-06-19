from request_study.api_ddatf.api.base_api import BaseApi
from request_study.api_ddatf.api.wework import WeWrok


class Tag(BaseApi):
    secrete = "E1H2f0zNzbTdCzjYBRzXgVs9LeCqGQvLH44VOQm-hFE"
    def __init__(self):
        self.token = WeWrok().get_token(self.secrete)["access_token"]
    def add(self,tag_name):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params":{
            "access_token":self.token
        },
            "json":{
                "group_name": "api",
                "tag": [{"name": tag_name}]
            }
        }
        return self.send_api(data)

    def get(self):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params":{
            "access_token":self.token
        },
            "json":{
               "tag_id": []
            }
        }
        return self.send_api(data)

    def delete(self,tag_id):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params":{
            "access_token":self.token
        },
            "json":{
               "tag_id": [tag_id]
            }
        }
        return self.send_api(data)

    def update(self,tag_id,tag_name):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params":{
            "access_token":self.token
        },
            "json":{
               "id": tag_id,
                "name":tag_name
            }
        }
        return self.send_api(data)