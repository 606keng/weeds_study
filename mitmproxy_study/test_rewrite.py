import json
from pprint import pprint


def response(flow):
    """
    对响应结果进行篡改
    :param flow:
    :return:
    """
    # pprint(flow.response.content)
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.text)
        data["data"]["items"][0]["quote"]["name"] = "榆林高氏集团"
        flow.response.text = json.dumps(data)