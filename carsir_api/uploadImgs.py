import requests
from requests_toolbelt import MultipartEncoder


def uploadImg(token, lenderInfoImgType, easyBuyId, agentId="edc8693c92cd4b40b25affe7d84386ec",
              url="https://test.carsir.xin/loan/AgentEasyBuyImgController/uploadImgs"):
    """
    上传图片通用接口
    :param token: 请求的token
    :param lenderInfoImgType: 上传图片的枚举值
    :param easyBuyId: 业务id
    :param agentId: 客户id
    :param url: 请求的URL
    :return:
    """
    headers = {
        "agentId": agentId,
        "token": token
    }
    #定义上传文件的路径
    files = "img/timg.jpg"
    #定义请求参数
    data = {
        "agentId": agentId,
        "lenderInfoImgType": lenderInfoImgType,
        "easyBuyId": easyBuyId,
        "files": ("1.jpg", open(files, "rb"), 'image/jpeg')
    }
    #将请求参数转换为数据流
    data = MultipartEncoder(data)
    #获取数据流的Content-Type
    headers["Content-Type"] = data.content_type
    r = requests.post(url=url, headers=headers, data=data)


# 1597224392 - 31507200