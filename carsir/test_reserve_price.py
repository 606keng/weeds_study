import pytest
import requests


class TestReservePrice:
    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "reservePriceLower","reservePriceHeight"], [
        ("30000", "10000", "2020-01-01" , "9000", "31800"),
        ("34800", "34800", "2019-12-31", "31400", "36800"),
        ("50000", "49900", "2018-01-01", "45000", "52500"),
        ("79900", "70000", "2020-01-01", "63000", "83800"),
        ("80000", "10000", "2018-01-01", "9000", "83200"),
        ("129000", "10000", "2019-01-01", "9000", "134100"),
        ("130000", "10000", "2020-01-01", "9000", "134500"),
        ("209900", "34800", "2019-12-31", "31400", "217200"),
        ("210000", "49900", "2018-01-01", "45000", "216300"),
        ("339900", "70000", "2020-01-01", "63000", "350000"),
        ("340000", "10000", "2018-01-01", "9000", "350200"),
        ("499900", "10000", "2019-01-01", "9000", "514800"),
            ])
    def test_less_three_price(self, purchasePrice, actualAmount, cardYear, reservePriceLower, reservePriceHeight):
        headers = {"token": "bbbb12303798418fae36fd19053e9c58",
                   "agentId":"037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type":"application/json; charset=utf-8"}
        url = "https://dev.carsir.xin/olympic/api-olympic-admin/priceCalculationController/priceCalculation"
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear":cardYear}
        r = requests.post(headers=headers, url=url, json=request_json, verify = False).json()
        assert str(int(r["data"]["reservePriceLower"])) == reservePriceLower
        assert str(int(r["data"]["reserverPriceUp"])) == reservePriceHeight


    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "reservePriceLower","reservePriceHeight"], [
        ("30000", "10000", "2017-01-01" , "9000", "32100"),
        ("34800", "34800", "2016-12-31", "31400", "37200"),
        ("50000", "49900", "2015-01-01", "45000", "53000"),
        ("79900", "70000", "2017-01-01", "63000", "84600"),
        ("80000", "10000", "2016-01-01", "9000", "84000"),
        ("129000", "10000", "2015-01-01", "9000", "135400"),
        ("130000", "10000", "2017-01-01", "9000", "135200"),
        ("209900", "34800", "2016-12-31", "31400", "218200"),
        ("210000", "49900", "2015-01-01", "45000", "217300"),
        ("339900", "70000", "2016-01-01", "63000", "351700"),
        ("340000", "10000", "2017-01-01", "9000", "350200"),
        ("499900", "10000", "2015-01-01", "9000", "514800"),
            ])
    def test_more_three_price(self, purchasePrice, actualAmount, cardYear, reservePriceLower, reservePriceHeight):
        headers = {"token": "bbbb12303798418fae36fd19053e9c58",
                   "agentId":"037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type":"application/json; charset=utf-8"}
        url = "https://dev.carsir.xin/olympic/api-olympic-admin/priceCalculationController/priceCalculation"
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear":cardYear}
        r = requests.post(headers=headers, url=url, json=request_json, verify = False).json()
        assert str(int(r["data"]["reservePriceLower"])) == reservePriceLower
        assert str(int(r["data"]["reserverPriceUp"])) == reservePriceHeight


    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "reservePriceLower","reservePriceHeight"], [
        ("30000", "10000", "2014-01-01" , "9000", "32400"),
        ("34800", "34800", "2013-12-31", "31400", "37500"),
        ("50000", "49900", "2012-01-01", "45000", "53500"),
        ("79900", "70000", "2011-01-01", "63000", "85400"),
        ("80000", "10000", "2010-01-01", "9000", "84800"),
        ("129900", "10000", "2014-01-01", "9000", "137600"),
        ("130000", "10000", "2013-01-01", "9000", "136500"),
        ("209900", "34800", "2012-12-31", "31400", "220300"),
        ("210000", "49900", "2011-01-01", "45000", "218400"),
        ("339900", "70000", "2010-01-01", "63000", "353400"),
        ("340000", "10000", "2011-01-01", "9000", "351900"),
        ("499900", "10000", "2010-01-01", "9000", "517300"),
            ])
    def test_more_five_price(self, purchasePrice, actualAmount, cardYear, reservePriceLower, reservePriceHeight):
        headers = {"token": "bbbb12303798418fae36fd19053e9c58",
                   "agentId":"037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type":"application/json; charset=utf-8"}
        url = "https://dev.carsir.xin/olympic/api-olympic-admin/priceCalculationController/priceCalculation"
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear":cardYear}
        r = requests.post(headers=headers, url=url, json=request_json, verify = False).json()
        assert str(r["data"]["reservePriceLower"]) == reservePriceLower
        assert str(r["data"]["reserverPriceUp"]) == reservePriceHeight


    @pytest.mark.parametrize(["purchasePrice", "actualAmount", "cardYear", "message"], [
        ("30000", "10000", "2009-01-01" , "车辆年限符合标准"),
        ("29999", "10000", "2010-01-01", "车辆年限符合标准"),
        ("500000", "10000", "2010-01-01", "车辆年限符合标准"),
            ])
    def test_error_price(self, purchasePrice, actualAmount, cardYear, message):
        headers = {"token": "bbbb12303798418fae36fd19053e9c58",
                   "agentId":"037e6d16010f11ea907c00163e129bed",
                   "grp": "carsir_app",
                   "Content-Type":"application/json; charset=utf-8"}
        url = "https://dev.carsir.xin/olympic/api-olympic-admin/priceCalculationController/priceCalculation"
        request_json = {"purchasePrice": purchasePrice, "actualAmount": actualAmount, "cardYear":cardYear}
        r = requests.post(headers=headers, url=url, json=request_json, verify = False).json()
        print(r)
        assert message == r["message"]