from carsir.easy_sell.api.addExamineOne import AddExamineOne
from carsir.easy_sell.api.base_api import BaseApi
from carsir.easy_sell.api.updateEasyBuyApplicantSecond import updateEasyBuyApplicantSecond


class TestRun(BaseApi):
    def test_submit_easy_buy(self):
         r = AddExamineOne().add_examine_one()
         print(r)
         easyBuyId = r["data"]["easyBuyId"]
         updateEasyBuyApplicantSecond(easyBuyId).upload_image()
         updateEasyBuyApplicantSecond(easyBuyId).update_easy_bug_applicant_second()