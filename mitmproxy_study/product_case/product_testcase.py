import os
import sys
from mitmproxy import http

# 获取当前文件运行的目录
addon_dir = os.path.dirname(__file__)
print(addon_dir)
# 将当前目录加入到环境变量中
sys.path.append(addon_dir)
# 导入Template
from template import Template


def response(flow: http.HTTPFlow):
    # 如果请求url中包含.json做如下操作
    if "https://api.carsir.xin/olympic/api-olympic-admin/my/car/listHomeCard" in flow.request.pretty_url:
        # 获取请求的方式
        method = flow.request.method
        print(method)
        # 获取请求的url，
        url = flow.request.pretty_url.split('?')[0]
        # 获取请求的参数,flow.request.query.fields返回的数据格式为二位元组，params为list[dict]
        # params = {k: v for k, v in flow.request.query.fields}

        # 获取请求的参数，并转换为字典
        data = eval(flow.request.text)
        # 获取请求cookie,flow.request.cookies.fields返回的数据格式为tuple(list)，cookies为list[dict]
        cookies = {k: v for k, v in flow.request.cookies.fields}

        # 获取请求的headers，返回的数据为bytes格式，需要使用.decode()转换为str
        headers = {k.decode(): v.decode() for k, v in flow.request.headers.fields}
        del headers[":authority"]
        data = {
            "method": method.__repr__(),
            "url": url.__repr__(),
            "data": [data],
            "cookies": [cookies],
            "headers": [headers]
        }
        # 使用模版引擎生成用例，test_http.mustache为目标，data为要生成的数据
        print(Template.render(addon_dir + "test_http.mustache", data))


if __name__ == '__main__':
    response()
