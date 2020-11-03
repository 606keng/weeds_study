from decimal import Decimal

import pytest
import requests
from carsir_test.easy_shou.amount_number import dispose_num_up, dispose_num_down


class TestReservePrice(object):
    """
    测试配资额上限
    """
    url = "https://test.carsir.xin/olympic/api-olympic-admin/priceCalculationController/rateCalculation"
    Authorization = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjA2NjY2NjY2NiIsInJvbGUiOiJST0xFX0NVU1RPTUVSIiwidG9rZW5faWQiOiJlOGYwMmZkMi1mYzE0LTRmMDctODhkNi01OGQ3ZTg3ZmE5ZWMiLCJpc3MiOiJBQ0NFU1MiLCJleHAiOjE2MDQ5NzU5MDgsImlhdCI6MTYwNDM3MTEwOH0.E38SLrw1OJV7k1Ol0TPMCEY8o_nrAAt67nopc3SPcDs9Fq3tXoaRssNruWindXoI46oiX01IWlRQgYnjBngxGg"
    public_rate = 0.9
    person_rate = 1
    public_car_info_id = "3546540c0d9946ef9b0aa85a86b604d6"
    person_car_info_id = "3f1a119e48004fea95f88e44847da1cd"

    @pytest.mark.parametrize(["purchasePrice", "usableAmount", "carInfoId","carPriceOver"], [
        ("30000", "1000000", public_car_info_id, "{}".format(dispose_num_down(30000*public_rate))),
        ("29800", "1000000", public_car_info_id, "{}".format(dispose_num_down(29800 * public_rate))),
        ("250000", "1000000", public_car_info_id, "{}".format(dispose_num_down(250000 * public_rate))),
        ("450000", "1000000", public_car_info_id, "{}".format(dispose_num_down(250000 * public_rate))),
        ("450000", "10000", public_car_info_id, "{}".format(dispose_num_down(10000 * public_rate))),
        ("29800", "10000", public_car_info_id, "{}".format(dispose_num_down(10000 * public_rate))),
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
        assert str(int(r["data"]["allocationLimit"])) == carPriceOver
    @pytest.mark.parametrize(["purchasePrice", "usableAmount", "carInfoId","carPriceOver"], [
        ("30000", "1000000", person_car_info_id, "{}".format(dispose_num_down(30000*person_rate))),
        ("29800", "1000000", person_car_info_id, "{}".format(dispose_num_down(29800 * person_rate))),
        ("250000", "1000000", person_car_info_id, "{}".format(dispose_num_down(250000 * person_rate))),
        ("450000", "1000000", person_car_info_id, "{}".format(dispose_num_down(250000 * person_rate))),
        ("450000", "10000", person_car_info_id, "{}".format(dispose_num_down(10000 * person_rate))),
        ("29800", "10000", person_car_info_id, "{}".format(dispose_num_down(10000 * person_rate))),
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