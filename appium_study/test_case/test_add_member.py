import pytest
import yaml

from appium_study.page.app import App


class TestAddMember():
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("username, gender, phone_number", yaml.safe_load(open("../data/contact.yml",encoding="utf-8")))
    def test_add_member(self,username,gender,phone_number):
        self.main.goto_addresslist().click_addmember().click_addmenual()\
            .input_name(username).set_gender(gender).input_phone(phone_number).click_save().veriy_toast().click_back()