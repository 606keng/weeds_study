import pytest
import requests

from carsir_test.easy_shou.amount_number import dispose_num_up


class TestPurchasingPrice(object):
    url = "https://test.carsir.xin/olympic/api-olympic-admin/workorder/check/test/getCarPrice1"
    token = "b17469d2b2ae4f00b755e4a977f9c374"
    # orderType = "QSP"

    ##########年限对应上限公式##############
    # ----------0 < year <=3----------
    # 车级S
    year_0_3_price_3_5_grade_s = 1.045
    year_0_3_price_5_8_grade_s = 1.042
    year_0_3_price_8_13_grade_s = 1.04
    year_0_3_price_13_21_grade_s = 1.036
    year_0_3_price_21_34_grade_s = 1.033
    year_0_3_price_34_50_grade_s = 1.03
    # 车级A
    year_0_3_price_3_5_grade_a = 1.028
    year_0_3_price_5_8_grade_a = 1.026
    year_0_3_price_8_13_grade_a = 1.025
    year_0_3_price_13_21_grade_a = 1.023
    year_0_3_price_21_34_grade_a = 1.021
    year_0_3_price_34_50_grade_a = 1.02
    # 车级B
    year_0_3_price_3_50_grade_b = 1

    # ----------3 < year <= 6----------
    # 车级S
    year_3_6_price_3_5_grade_s = 1.0225
    year_3_6_price_5_8_grade_s = 1.021
    year_3_6_price_8_13_grade_s = 1.02
    year_3_6_price_13_21_grade_s = 1.018
    year_3_6_price_21_34_grade_s = 1.065
    year_3_6_price_34_50_grade_s = 1.05
    # 车级A
    year_3_6_price_3_5_grade_a = 1.014
    year_3_6_price_5_8_grade_a = 1.013
    year_3_6_price_8_13_grade_a = 1.025
    year_3_6_price_13_21_grade_a = 1.015
    year_3_6_price_21_34_grade_a = 1.005
    year_3_6_price_34_50_grade_a = 1.01
    # 车级B
    year_3_6_price_3_50_grade_b = 1

    # ----------6 < year <= 10----------
    # 车级S
    year_6_10_price_3_50_grade_s = 1
    # 车级A
    year_6_10_price_3_50_grade_a = 1
    # 车级B
    year_6_10_price_3_50_grade_b = 1

    # >10年 给与不符合准入标注提示

    # ----------0 < year <=3----------
    @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
        # 车级S
        ("30000", "2020-01-01", "{}".format(dispose_num_up(30000 * year_0_3_price_3_5_grade_s))),
        # ("34000", "2019-12-31", "{}".format(dispose_num_up(34000 * year_0_3_price_3_5_grade_s))),
        # ("50000", "2019-01-31", "{}".format(dispose_num_up(50000 * year_0_3_price_5_8_grade_s))),
        # ("79900", "2018-12-31", "{}".format(dispose_num_up(79900 * year_0_3_price_5_8_grade_s))),
        # ("80000", "2018-01-01", "{}".format(dispose_num_up(80000 * year_0_3_price_8_13_grade_s))),
        # ("129000", "2019-01-01", "{}".format(dispose_num_up(129000 * year_0_3_price_8_13_grade_s))),
        # ("130000", "2020-01-01", "{}".format(dispose_num_up(130000 * year_0_3_price_13_21_grade_s))),
        # ("209900", "2019-12-31", "{}".format(dispose_num_up(209900 * year_0_3_price_13_21_grade_s))),
        # ("210000", "2018-01-01", "{}".format(dispose_num_up(210000 * year_0_3_price_21_34_grade_s))),
        # ("339900", "2020-01-01", "{}".format(dispose_num_up(339900 * year_0_3_price_21_34_grade_s))),
        # ("340000", "2018-01-01", "{}".format(dispose_num_up(340000 * year_0_3_price_34_50_grade_s))),
        # ("499900", "2019-01-01", "{}".format(dispose_num_up(499900 * year_0_3_price_34_50_grade_s))),
    ])
    def test_less_three_price_s(self, purchasePrice, cardYear, reservePrice):
        """
        上牌时限小于3年,且车的检测级别为S
        """
        headers = {"token": self.token,
                   # "Content-Type": "application/json; charset=utf-8",
                   "grp": "nba_pc"
                   # "version": "20191115",
                   }
        request_json = {"car300": purchasePrice, "year": cardYear,
                        "carLevel": "s"}
        r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
        assert str(r["data"]) == reservePrice
    #
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级A
    #     ("30000", "2020-01-01", "{}".format(dispose_num_up(30000 * year_0_3_price_3_5_grade_a))),
    #     ("34000", "2019-12-31", "{}".format(dispose_num_up(34000 * year_0_3_price_3_5_grade_a))),
    #     ("50000", "2019-01-31", "{}".format(dispose_num_up(50000 * year_0_3_price_5_8_grade_a))),
    #     ("79900", "2018-12-31", "{}".format(dispose_num_up(79900 * year_0_3_price_5_8_grade_a))),
    #     ("80000", "2018-01-01", "{}".format(dispose_num_up(80000 * year_0_3_price_8_13_grade_a))),
    #     ("129000", "2019-01-01", "{}".format(dispose_num_up(129000 * year_0_3_price_8_13_grade_a))),
    #     ("130000", "2020-01-01", "{}".format(dispose_num_up(130000 * year_0_3_price_13_21_grade_a))),
    #     ("209900", "2019-12-31", "{}".format(dispose_num_up(209900 * year_0_3_price_13_21_grade_a))),
    #     ("210000", "2018-01-01", "{}".format(dispose_num_up(210000 * year_0_3_price_21_34_grade_a))),
    #     ("339900", "2020-01-01", "{}".format(dispose_num_up(339900 * year_0_3_price_21_34_grade_a))),
    #     ("340000", "2018-01-01", "{}".format(dispose_num_up(340000 * year_0_3_price_34_50_grade_a))),
    #     ("499900", "2019-01-01", "{}".format(dispose_num_up(499900 * year_0_3_price_34_50_grade_a))),
    # ])
    # def test_less_three_price_a(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限小于3年,且车的检测级别为A
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "A"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级B
    #     ("30000", "2020-01-01", "{}".format(dispose_num_up(30000 * year_0_3_price_3_50_grade_b))),
    #     ("499900", "2018-01-01", "{}".format(dispose_num_up(499900 * year_0_3_price_3_50_grade_b))),
    # ])
    # def test_less_three_price_b(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限小于3年,且车的检测级别为B
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "B"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # # ----------3 < year <= 6----------
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级S
    #     ("30000", "2017-01-01", "{}".format(dispose_num_up(30000 * year_3_6_price_3_5_grade_s))),
    #     ("34000", "2015-12-31", "{}".format(dispose_num_up(34000 * year_3_6_price_3_5_grade_s))),
    #     ("50000", "2016-01-01", "{}".format(dispose_num_up(50000 * year_3_6_price_5_8_grade_s))),
    #     ("79900", "2016-01-01", "{}".format(dispose_num_up(79900 * year_3_6_price_5_8_grade_s))),
    #     ("80000", "2017-01-01", "{}".format(dispose_num_up(80000 * year_3_6_price_8_13_grade_s))),
    #     ("129000", "2015-01-01", "{}".format(dispose_num_up(129000 * year_3_6_price_8_13_grade_s))),
    #     ("130000", "2016-01-01", "{}".format(dispose_num_up(130000 * year_3_6_price_13_21_grade_s))),
    #     ("209900", "2017-12-31", "{}".format(dispose_num_up(209900 * year_3_6_price_13_21_grade_s))),
    #     ("210000", "2015-01-01", "{}".format(dispose_num_up(210000 * year_3_6_price_21_34_grade_s))),
    #     ("339900", "2016-01-01", "{}".format(dispose_num_up(339900 * year_3_6_price_21_34_grade_s))),
    #     ("340000", "2017-01-01", "{}".format(dispose_num_up(340000 * year_3_6_price_34_50_grade_s))),
    #     ("499900", "2015-01-01", "{}".format(dispose_num_up(499900 * year_3_6_price_34_50_grade_s))),
    # ])
    # def test_more_three_price_s(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限大于3年，小于6年,且车的检测级别为S
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "S"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级A
    #     ("30000", "2017-01-01", "{}".format(dispose_num_up(30000 * year_3_6_price_3_5_grade_a))),
    #     ("34000", "2015-12-31", "{}".format(dispose_num_up(34000 * year_3_6_price_3_5_grade_a))),
    #     ("50000", "2016-01-01", "{}".format(dispose_num_up(50000 * year_3_6_price_5_8_grade_a))),
    #     ("79900", "2016-01-01", "{}".format(dispose_num_up(79900 * year_3_6_price_5_8_grade_a))),
    #     ("80000", "2017-01-01", "{}".format(dispose_num_up(80000 * year_3_6_price_8_13_grade_a))),
    #     ("129000", "2015-01-01", "{}".format(dispose_num_up(129000 * year_3_6_price_8_13_grade_a))),
    #     ("130000", "2016-01-01", "{}".format(dispose_num_up(130000 * year_3_6_price_13_21_grade_a))),
    #     ("209900", "2017-12-31", "{}".format(dispose_num_up(209900 * year_3_6_price_13_21_grade_a))),
    #     ("210000", "2015-01-01", "{}".format(dispose_num_up(210000 * year_3_6_price_21_34_grade_a))),
    #     ("339900", "2016-01-01", "{}".format(dispose_num_up(339900 * year_3_6_price_21_34_grade_a))),
    #     ("340000", "2017-01-01", "{}".format(dispose_num_up(340000 * year_3_6_price_34_50_grade_a))),
    #     ("499900", "2015-01-01", "{}".format(dispose_num_up(499900 * year_3_6_price_34_50_grade_a))),
    # ])
    # def test_more_three_price_a(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限大于3年，小于6年,且车的检测级别为A
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "A"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级B
    #     ("30000", "2017-01-01", "{}".format(dispose_num_up(30000 * year_3_6_price_3_50_grade_b))),
    #     ("499900", "2015-01-01", "{}".format(dispose_num_up(499900 * year_3_6_price_3_50_grade_b))),
    # ])
    # def test_more_three_price_b(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限大于3年，小于6年,且车的检测级别为B
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "B"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # # ----------6 < year <= 10----------
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级S
    #     ("30000", "2017-01-01", "{}".format(dispose_num_up(30000 * year_6_10_price_3_50_grade_s))),
    #     ("490000", "2011-01-01", "{}".format(dispose_num_up(490000 * year_6_10_price_3_50_grade_s)))
    # ])
    # def test_more_six_price_s(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限大于6年，小于10年,且车的检测级别为S
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "S"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级A
    #     ("30000", "2017-01-01", "{}".format(dispose_num_up(30000 * year_6_10_price_3_50_grade_a))),
    #     ("490000", "2011-01-01", "{}".format(dispose_num_up(490000 * year_6_10_price_3_50_grade_a)))
    # ])
    # def test_more_six_price_a(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限大于6年，小于10年,且车的检测级别为A
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "A"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "reservePrice"], [
    #     # 车级B
    #     ("30000", "2017-01-01", "{}".format(dispose_num_up(30000 * year_6_10_price_3_50_grade_b))),
    #     ("490000", "2011-01-01", "{}".format(dispose_num_up(490000 * year_6_10_price_3_50_grade_b)))
    # ])
    # def test_more_six_price_b(self, purchasePrice, cardYear, reservePrice, orderType=orderType):
    #     """
    #     上牌时限大于3年，小于6年,且车的检测级别为B
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "B"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert str(int(r["data"]["..."])) == reservePrice
    #
    # # 异常测试-1
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "message"], [
    #     # 小于30000，大于500000
    #     ("29000", "2020-01-01", "很抱歉，车辆不符合准入标准"),
    #     ("500000", "2020-01-01", "很抱歉，车辆不符合准入标准")
    # ])
    # def test_error_price(self, purchasePrice, cardYear, message, orderType=orderType):
    #     """
    #     # 车辆价值小于30000，大于500000
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "S"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert r["message"] == message
    #
    # # 异常测试-2
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "message"], [
    #     # 年限大于10年-S级车
    #     ("490000", "2010-01-01", "很抱歉，车辆不符合准入标准")
    # ])
    # def test_error_year_s(self, purchasePrice, cardYear, message, orderType=orderType):
    #     """
    #     # 车辆年限大于10年-S级车
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "S"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert r["message"] == message
    #
    # # 异常测试-3
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "message"], [
    #     # 年限大于10年-S级车
    #     ("490000", "2010-01-01", "很抱歉，车辆不符合准入标准")
    # ])
    # def test_error_year_a(self, purchasePrice, cardYear, message, orderType=orderType):
    #     """
    #     # 车辆年限大于10年-A级车
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "A"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert r["message"] == message
    #
    # # 异常测试-4
    # @pytest.mark.parametrize(["purchasePrice", "cardYear", "message"], [
    #     # 年限大于10年-B级车
    #     ("490000", "2010-01-01", "很抱歉，车辆不符合准入标准")
    # ])
    # def test_error_year_b(self, purchasePrice, cardYear, message, orderType=orderType):
    #     """
    #     # 车辆年限大于10年-S级车
    #     """
    #     headers = {"token": self.token,
    #                "Content-Type": "application/json; charset=utf-8",
    #                "grp": "nba_pc",
    #                "version": "20191115",
    #                "userId": "",
    #                "grade": "B"
    #                }
    #     request_json = {"purchasePrice": purchasePrice, "cardYear": cardYear,
    #                     "orderType": orderType}
    #     r = requests.post(headers=headers, url=self.url, json=request_json, verify=False).json()
    #     print(r)
    #     assert r["message"] == message

if __name__ == '__main__':
    test = TestPurchasingPrice()
    test.test_less_three_price_s()
    # test.test_less_three_price_a()
    # test.test_less_three_price_b()
    # test.test_more_three_price_s()
    # test.test_more_three_price_a()
    # test.test_more_three_price_b()
    # test.test_more_six_price_s()
    # test.test_more_six_price_a()
    # test.test_more_six_price_b()
    # test.test_error_price()
    # test.test_error_year_s()
    # test.test_error_year_a()
    # test.test_error_year_b()