"""
在请求之前，对请求的URL进行替换
1.需要二次封装requests，对请求进行定制化
2.将请求的结构体的URL从一个写死的IP地址改为一个（任意的）域名
3.使用一个env配置文件，存放各个环境的配置信息
4.将请求体中的URL替换为env配置文件中个人选择的URL
5.将env配置文件用yaml进行管理
"""
import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data: dict):
        #替换，self.env["environment"][self.env["default"]]等同于self.env["environment"]["dev"]
        data["url"] = str(data['url']).replace("test",self.env["environment"][self.env["default"]])
        print(data["url"])
        res = requests.request(method=data["method"],
                         url=data["url"],
                         headers=data["headers"])
        return res.text