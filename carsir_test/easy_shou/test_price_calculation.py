from decimal import Decimal

import pytest
import requests
from carsir_test.easy_shou.amount_number import dispose_num_up, dispose_num_down


class TestReservePrice(object):
    """
    测试配资额上限
    """
    url = "https://test.carsir.xin/olympic/api-olympic-admin/priceCalculationController/rateCalculation"
    Authorization = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjA0NDQ0NDQ0NCIsInJvbGUiOiJST0xFX0NVU1RPTUVSIiwidG9rZW5faWQiOiIyZGI5MWFkNC1iNTRmLTRlNDItYjc0ZS1kZDNjNjliOTZkNjgiLCJpc3MiOiJBQ0NFU1MiLCJleHAiOjE2MDY5ODUxNTAsImlhdCI6MTYwNjM4MDM1MH0.CypG8WhlidjTJ5QCZGIBf-OlO62SL6jV4CfXAQpPJ3jP4qq-bFyAyUEqNGsnRyLtZ-Fv8YEOiZtDOxrr2U2CEw"
    public_rate = 0.9
    person_rate = 1
    public_car_info_id = "120d62ee48264626ace54e952be0f210"
    person_car_info_id = "d8a0337597b8451bb0eb09c58a273197"

    @pytest.mark.parametrize(["purchasePrice", "usableAmount", "carInfoId","carPriceOver"], [
        ("30000", "1000000", public_car_info_id, "{}".format(dispose_num_down(30000*public_rate))),
        ("29800", "1000000", public_car_info_id, "{}".format(dispose_num_down(29800 * public_rate))),
        ("250000", "1000000", public_car_info_id, "{}".format(dispose_num_down(250000 * public_rate))),
        ("450000", "1000000", public_car_info_id, "{}".format(dispose_num_down(250000))),
        ("270000", "1000000", public_car_info_id, "{}".format(dispose_num_down(270000 * public_rate))),
        ("450000", "10000", public_car_info_id, "{}".format(dispose_num_down(10000 ))),
        ("29800", "10000", public_car_info_id, "{}".format(dispose_num_down(10000))),
    ])
    def test_public_car(self, purchasePrice, usableAmount, carInfoId, carPriceOver):
        """

        :param purchasePrice:
        :param usableAmount:
        :param carInfoId:
        :param carPriceOver:
        :return:
        """
        headers = {"Authorization": self.Authorization,
                   "agentId": "037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type": "application/json; charset=utf-8"}
        request_json = {"purchasePrice": purchasePrice, "usableAmount": usableAmount, "carInfoId": carInfoId}
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        print(r)
        assert str(int(r["data"]["allocationLimit"])) == carPriceOver
    @pytest.mark.parametrize(["purchasePrice", "usableAmount", "carInfoId","carPriceOver"], [
        ("30000", "1000000", person_car_info_id, "{}".format(dispose_num_down(30000*person_rate))),
        ("29800", "1000000", person_car_info_id, "{}".format(dispose_num_down(29800 * person_rate))),
        ("250000", "1000000", person_car_info_id, "{}".format(dispose_num_down(250000 * person_rate))),
        ("450000", "1000000", person_car_info_id, "{}".format(dispose_num_down(250000 * person_rate))),
        ("450000", "10000", person_car_info_id, "{}".format(dispose_num_down(10000))),
        ("29800", "10000", person_car_info_id, "{}".format(dispose_num_down(10000))),
    ])
    def test_person_car(self, purchasePrice, usableAmount, carInfoId, carPriceOver):
        """

        :param purchasePrice:
        :param usableAmount:
        :param carInfoId:
        :param carPriceOver:
        :return:
        """
        headers = {"Authorization": self.Authorization,
                   "agentId": "037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type": "application/json; charset=utf-8"}
        request_json = {"purchasePrice": purchasePrice, "usableAmount": usableAmount, "carInfoId": carInfoId}
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        assert str(int(r["data"]["allocationLimit"])) == carPriceOver