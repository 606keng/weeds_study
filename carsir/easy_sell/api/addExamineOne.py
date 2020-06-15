from carsir.easy_sell.api.base_api import BaseApi
from carsir.easy_sell.api.login import Login


class AddExamineOne(BaseApi):
    """
    提交贷款人身份信息
    """
    def __init__(self):
        r = Login().get_carsir_token()
        self.token = r["data"]["users"]["token"]
        self.agentId = r["data"]["users"]["agentId"]
        self.file1 = r"D:\work\auto\weeds_study\carsir\easy_sell\img\timg.jpg"
    def add_examine_one(self):
        data = {
            "method": "post",
            "url": "https://test.carsir.xin/loan/AgentEasyBuyController/addExamineOne",
            "headers": {
                "token": self.token,
                "agentId":self.agentId,
                "User-Agent":"okhttp/3.12.1"
            },
            "data": {
                "lenderSex": "1",
                "agentId":self.agentId,
                "productId":"4",
                "cityCode":"610116",
                "lenderInfoImgType":"1",
                "lenderAge":"28",
                "sercenterName":"西安天府-兜兜捏",
                "lenderDataForBrith":"19951016",
                "productName":"华夏银行",
                "sercenterId":"f6604930da02477f86a935519ef5269d",
                "lenderIdcard":"610481199210165431",
                "lenderName":"豆高",
                "operationType":"2",
                "file1": ("1.jpg", open(self.file1, "rb"), 'image/jpeg'),
                "file2": ("2.jpg", open(self.file1, "rb"), 'image/jpeg')
            }
        }
        return self.send_api_upload(data)