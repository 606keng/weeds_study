import json
from pprint import pprint


def response(flow):
    """
    对响应结果进行篡改
    :param flow:
    :return:
    """
    # pprint(flow.response.content)
    if "client.action?functionId=wareBusines" in flow.request.pretty_url:
        print(flow.request.content)
        # data = json.loads(flow.request.content)
        #
        # data["serviceAreaId"] = "130100"
        # pprint(data)
        # serviceAreaId
        data = json.loads(flow.response.text)
        pprint(data)
        data["floors"][29]["data"]["yuyueInfo"]["startTime"] = 1603331880
        # data["currentTime"] = 1603172400000
        # data["skuList"][0]["panicbuyingStartTime"] = 1603172400000
        flow.response.text = json.dumps(data)
