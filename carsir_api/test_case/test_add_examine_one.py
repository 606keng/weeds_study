from carsir_test.easy_sell.api.addExamineOne import AddExamineOne
from carsir_test.easy_sell.api.base_api import BaseApi


class TestAddExamineOne(BaseApi):
    def test_add_examine_one(self):
        """
        上传个人信息，提交轻松卖待初审订单
        :return:
        """
        print(AddExamineOne().add_examine_one())