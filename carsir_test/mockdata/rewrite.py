import json
from pprint import pprint


def response(flow):
    """
    对响应结果进行篡改
    :param flow:
    :return:
    """
    # pprint(flow.response.content)
    if "/olympic/api-olympic-admin/easySell/carSource/inStockCarSourceList" in flow.request.pretty_url:
        data = json.loads(flow.response.text)
        data["data"]["records"][2]["sharingCenterName"] = "carsir日照共享中心carsir日照共享中心carsir日照共享中心"
        # data["data"]["records"][0]["carNature"]= "PERSONAL"
        # data["data"]["records"][1]["carNature"] = "PUBLIC"
        pprint(data)
        flow.response.text = json.dumps(data)
