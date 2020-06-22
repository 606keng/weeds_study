from carsir_api.api.base_api import BaseApi
from carsir_api.api.login_page.login import Login
from carsir_api.utils.basepath import BasePath


class AddExamineOne(BaseApi):
    """
    提交贷款人身份信息
    """
    def __init__(self):
        r = Login().get_carsir_token()
        self.token = r["data"]["users"]["token"]
        self.agentId = r["data"]["users"]["agentId"]
        self.file1 = BasePath+r"\data\timg.jpg"
    def add_examine_one(self):
        data = {
            "method": "post",
            "url": "https://carsir_host/loan/AgentEasyBuyController/addExamineOne",
            "headers": {
                "token": self.token,
                "agentId":self.agentId,
                "User-Agent":"okhttp/3.12.1"
            },
            "data": {
                "lenderSex": "1",
                "agentId":self.agentId,
                "productId":"4",
                "cityCode":"450302",
                "lenderInfoImgType":"1",
                "lenderAge":"28",
                "sercenterName":"服务中心测试-Pre-L0001",
                "lenderDataForBrith":"19951016",
                "productName":"轻松购一期产品",
                "sercenterId":"268eec2ba97c4cfeb7804ed24db1234d",
                "lenderIdcard":"610481199210165431",
                "lenderName":"豆高",
                "operationType":"2",
                "file1": ("1.jpg", open(self.file1, "rb"), 'image/jpeg'),
                "file2": ("2.jpg", open(self.file1, "rb"), 'image/jpeg')
            }
        }
        return self.send_api_upload(data)