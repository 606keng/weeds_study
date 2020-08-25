from decimal import Decimal

import pytest
import requests
from carsir_test.easy_shou.amount_number import dispose_num_up, dispose_num_down


class TestReservePrice(object):
    """
     测试轻松配保留价上限
    """
    url = "https://pre.carsir.xin/olympic/api-olympic-admin/priceCalculationController/priceCalculation"
    token = "f35ba147dbac4eef91294d9ee6f135f1"
    orderType = "QSP"
    rate = 1
    year_0_3_price_3_5 = Decimal("1.12")
    year_0_3_price_5_8 = Decimal("1.11")
    year_0_3_price_8_13 = Decimal("1.1")
    year_0_3_price_13_21 = Decimal("1.095")
    year_0_3_price_21_34 = Decimal("1.09")
    year_0_3_price_34_50 = Decimal("1.09")

    year_3_6_price_3_5 = Decimal("1.13")
    year_3_6_price_5_8 = Decimal("1.12")
    year_3_6_price_8_13 = Decimal("1.11")
    year_3_6_price_13_21 = Decimal("1.1")
    year_3_6_price_21_34 = Decimal("1.095")
    year_3_6_price_34_50 = Decimal("1.09")

    year_6_10_price_3_5 = Decimal("1.14")
    year_6_10_price_5_8 = Decimal("1.13")
    year_6_10_price_8_13 = Decimal("1.12")
    year_6_10_price_13_21 = Decimal("1.11")
    year_6_10_price_21_34 = Decimal("1.10")
    year_6_10_price_34_50 = Decimal("1.095")

    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "reservePriceLower", "reservePriceHeight"], [
        ("30000", "10000", "2020-01-01", "{}".format(dispose_num_up(30000 * rate)),
         "{}".format(dispose_num_down(30000 * year_0_3_price_3_5))),
        ("34800", "34800", "2019-12-31", "{}".format(dispose_num_up(34800 * rate)),
         "{}".format(dispose_num_down(34800 * year_0_3_price_3_5))),
        ("50000", "49900", "2018-01-01", "{}".format(dispose_num_up(50000 * rate)),
         "{}".format(dispose_num_down(50000 * year_0_3_price_5_8))),
        ("79900", "70000", "2020-01-01", "{}".format(dispose_num_up(79900 * rate)),
         "{}".format(dispose_num_down(79900 * year_0_3_price_5_8))),
        ("80000", "10000", "2018-01-01", "{}".format(dispose_num_up(80000 * rate)),
         "{}".format(dispose_num_down(80000 * year_0_3_price_8_13))),
        ("129000", "10000", "2019-01-01", "{}".format(dispose_num_up(129000 * rate)),
         "{}".format(dispose_num_down(129000 * year_0_3_price_8_13))),
        ("130000", "10000", "2020-01-01", "{}".format(dispose_num_up(130000 * rate)),
         "{}".format(dispose_num_down(130000 * year_0_3_price_13_21))),
        ("209900", "34800", "2017-12-31", "{}".format(dispose_num_up(209900 * rate)),
         "{}".format(dispose_num_down(209900 * year_0_3_price_13_21))),
        ("210000", "49900", "2018-01-01", "{}".format(dispose_num_up(210000 * rate)),
         "{}".format(dispose_num_down(210000 * year_0_3_price_21_34))),
        ("339900", "70000", "2017-01-01", "{}".format(dispose_num_up(339900 * rate)),
         "{}".format(dispose_num_down(339900 * year_0_3_price_21_34))),
        ("340000", "10000", "2018-01-01", "{}".format(dispose_num_up(340000 * rate)),
         "{}".format(dispose_num_down(340000 * year_0_3_price_34_50))),
        ("499900", "10000", "2019-01-01", "{}".format(dispose_num_up(499900 * rate)),
         "{}".format(dispose_num_down(499900 * year_0_3_price_34_50))),
    ])
    def test_less_three_price(self, purchasePrice, actualAmount, cardYear, reservePriceLower, reservePriceHeight,
                              orderType=orderType):
        """
        上牌年限小于3年
        :param purchasePrice:
        :param actualAmount:
        :param cardYear:
        :param reservePriceLower:
        :param reservePriceHeight:
        :return:
        """
        headers = {"token": self.token,
                   "agentId": "037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type": "application/json; charset=utf-8"}
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear": cardYear,
                        "orderType": orderType}
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        print(r)
        assert str(int(r["data"]["reserverPriceUp"])) == reservePriceHeight
        assert str(int(r["data"]["reservePriceLower"])) == reservePriceLower

    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "reservePriceLower", "reservePriceHeight"], [
        ("30000", "10000", "2014-01-01", "{}".format(dispose_num_up(30000 * rate)),
         "{}".format(dispose_num_down(30000 * year_3_6_price_3_5))),
        ("34800", "34800", "2015-12-31", "{}".format(dispose_num_up(34800 * rate)),
         "{}".format(dispose_num_down(34800 * year_3_6_price_3_5))),
        ("50000", "49900", "2016-01-01", "{}".format(dispose_num_up(50000 * rate)),
         "{}".format(dispose_num_down(50000 * year_3_6_price_5_8))),
        ("79900", "70000", "2016-01-01", "{}".format(dispose_num_up(79900 * rate)),
         "{}".format(dispose_num_down(79900 * year_3_6_price_5_8))),
        ("80000", "10000", "2014-01-01", "{}".format(dispose_num_up(80000 * rate)),
         "{}".format(dispose_num_down(80000 * year_3_6_price_8_13))),
        ("129000", "10000", "2015-01-01", "{}".format(dispose_num_up(129000 * rate)),
         "{}".format(dispose_num_down(129000 * year_3_6_price_8_13))),
        ("130000", "10000", "2016-01-01", "{}".format(dispose_num_up(130000 * rate)),
         "{}".format(dispose_num_down(130000 * year_3_6_price_13_21))),
        ("209900", "34800", "2014-12-31", "{}".format(dispose_num_up(209900 * rate)),
         "{}".format(dispose_num_down(209900 * year_3_6_price_13_21))),
        ("210000", "49900", "2015-01-01", "{}".format(dispose_num_up(210000 * rate)),
         "{}".format(dispose_num_down(210000 * year_3_6_price_21_34))),
        ("339900", "70000", "2016-01-01", "{}".format(dispose_num_up(339900 * rate)),
         "{}".format(dispose_num_down(339900 * year_3_6_price_21_34))),
        ("340000", "10000", "2014-01-01", "{}".format(dispose_num_up(340000 * rate)),
         "{}".format(dispose_num_down(340000 * year_3_6_price_34_50))),
        ("499900", "10000", "2015-01-01", "{}".format(dispose_num_up(499900 * rate)),
         "{}".format(dispose_num_down(499900 * year_3_6_price_34_50))),
    ])
    def test_more_three_price(self, purchasePrice, actualAmount, cardYear, reservePriceLower, reservePriceHeight,
                              orderType=orderType):
        """
        上牌年限大于等于3年，小于6年
        :param purchasePrice:
        :param actualAmount:
        :param cardYear:
        :param reservePriceLower:
        :param reservePriceHeight:
        :return:
        """
        headers = {"token": self.token,
                   "agentId": "037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type": "application/json; charset=utf-8"}
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear": cardYear,
                        "orderType": orderType}
        print(request_json)
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        assert str(int(r["data"]["reserverPriceUp"])) == reservePriceHeight
        assert str(int(r["data"]["reservePriceLower"])) == reservePriceLower

    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "reservePriceLower", "reservePriceHeight"], [
        ("30000", "10000", "2010-01-01", "{}".format(dispose_num_up(30000 * rate)),
         "{}".format(dispose_num_down(30000 * year_6_10_price_3_5))),
        ("34800", "34800", "2013-12-31", "{}".format(dispose_num_up(34800 * rate)),
         "{}".format(dispose_num_down(34800 * year_6_10_price_3_5))),
        ("50000", "49900", "2012-01-01", "{}".format(dispose_num_up(50000 * rate)),
         "{}".format(dispose_num_down(50000 * year_6_10_price_5_8))),
        ("79900", "70000", "2011-01-01", "{}".format(dispose_num_up(79900 * rate)),
         "{}".format(dispose_num_down(79900 * year_6_10_price_5_8))),
        ("80000", "10000", "2010-01-01", "{}".format(dispose_num_up(80000 * rate)),
         "{}".format(dispose_num_down(80000 * year_6_10_price_8_13))),
        ("129000", "10000", "2011-01-01", "{}".format(dispose_num_up(129000 * rate)),
         "{}".format(dispose_num_down(129000 * year_6_10_price_8_13))),
        ("130000", "10000", "2013-01-01", "{}".format(dispose_num_up(130000 * rate)),
         "{}".format(dispose_num_down(130000 * year_6_10_price_13_21))),
        ("209900", "34800", "2012-12-31", "{}".format(dispose_num_up(209900 * rate)),
         "{}".format(dispose_num_down(209900 * year_6_10_price_13_21))),
        ("210000", "49900", "2011-01-01", "{}".format(dispose_num_up(210000 * rate)),
         "{}".format(dispose_num_down(210000 * year_6_10_price_21_34))),
        ("339900", "70000", "2010-01-01", "{}".format(dispose_num_up(339900 * rate)),
         "{}".format(dispose_num_down(339900 * year_6_10_price_21_34))),
        ("340000", "10000", "2013-01-01", "{}".format(dispose_num_up(340000 * rate)),
         "{}".format(dispose_num_down(340000 * year_6_10_price_34_50))),
        ("499900", "10000", "2011-01-01", "{}".format(dispose_num_up(499900 * rate)),
         "{}".format(dispose_num_down(499900 * year_6_10_price_34_50))),
        ("500000", "10000", "2011-01-01", "{}".format(dispose_num_up(500000 * rate)),
         "{}".format(dispose_num_down(500000 * year_6_10_price_34_50))),
    ])
    def test_more_six_price(self, purchasePrice, actualAmount, cardYear, reservePriceLower, reservePriceHeight,
                            orderType=orderType):
        headers = {"token": self.token,
                   "agentId": "037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type": "application/json; charset=utf-8"}
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear": cardYear,
                        "orderType": orderType}
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        assert str(int(r["data"]["reserverPriceUp"])) == reservePriceHeight
        assert str(int(r["data"]["reservePriceLower"])) == reservePriceLower

    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "message"], [
        ("30000", "10000", "2009-01-01", "车辆年限不符合标准"),
        ("29999", "10000", "2010-01-01", "车辆不符合标准"),
        ("500100", "10000", "2010-01-01", "车辆不符合标准"),
    ])
    def test_error_price(self, purchasePrice, actualAmount, cardYear, message, orderType=orderType):
        headers = {"token": self.token,
                   "agentId": "037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type": "application/json; charset=utf-8"}
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear": cardYear,
                        "orderType": orderType}
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        print(r)
        assert message == r["message"]


if __name__ == '__main__':
    test = TestReservePrice()
    test.test_less_three_price()
    test.test_more_three_price()
    test.test_more_five_price()
    test.test_error_price()
