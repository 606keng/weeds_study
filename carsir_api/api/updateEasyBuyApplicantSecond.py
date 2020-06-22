from carsir_api.api.base_api import BaseApi
from carsir_api.api.login_page.login import Login
from carsir_api.utils.basepath import BasePath


class updateEasyBuyApplicantSecond(BaseApi):
    """
    创建轻松购订单
    """
    def __init__(self,easyBuyId):
        r = Login().get_carsir_token()
        self.token = r["data"]["users"]["token"]
        self.agentId = r["data"]["users"]["agentId"]
        self.file1 = BasePath+r"\data\timg.jpg"
        self.easyBuyId = easyBuyId
    def upload_image(self):
        ImgTypes = [2,3,4,5,6,7]
        for ImgType in ImgTypes:
            data = {
                "method": "post",
                "url": "https://carsir_host/loan/AgentEasyBuyImgController/uploadImgs",
                "headers": {
                    "token": self.token,
                    "agentId":self.agentId
                },
                "data": {
                    "agentId": self.agentId,
                    "lenderInfoImgType": str(ImgType),
                    "easyBuyId": self.easyBuyId,
                    "files": ("1.jpg", open(self.file1, "rb"), 'image/jpeg')
                }
            }
            self.send_api_upload(data)

    def update_easy_bug_applicant_second(self):
        data = {
            "method": "post",
            "url": "https://carsir_host/loan/AgentEasyBuyController/updateEasyBuyApplicantSecond",
            "headers": {
                "token": self.token,
                "agentId":self.agentId,
                "Content-Type":"application/x-www-form-urlencoded"
            },
            "data": {'agentId': self.agentId,
                     'agentName': '豆立航',
                     'authentBankCard': '64646',
                     'authentBankPhone': '18791076614',
                     'cityCode': '610116',
                     'easyBuyId': self.easyBuyId,
                     'lenderIdcardAddress': '610481199210165431',
                     'maritalStatus': '1',
                     'operatorTel': '是',
                     'preApprovedLoanAmount': '4557676'
                     }
        }
        return self.send_api(data)