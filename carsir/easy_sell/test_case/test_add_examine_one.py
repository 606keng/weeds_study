from carsir.easy_sell.api.addExamineOne import AddExamineOne
from carsir.easy_sell.api.base_api import BaseApi


class TestAddExamineOne(BaseApi):
    def test_add_examine_one(self):
        print(AddExamineOne().add_examine_one())