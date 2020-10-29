import json
from pprint import pprint


def response(flow):
    """
    对响应结果进行篡改
    :param flow:
    :return:
    """
    # pprint(flow.response.content)
    if "/olympic/api-olympic-admin/redeemorder/getRedeemOrderInfo" in flow.request.pretty_url:
        print(flow.request.content)
        # data = json.loads(flow.request.content)
        #
        # data["serviceAreaId"] = "130100"
        # pprint(data)
        # serviceAreaId
        try:
            data = json.loads(flow.response.text)
            pprint(data)
            data["data"]['lateFee'] = None
            flow.response.text = json.dumps(data)
        except:
            pass



















