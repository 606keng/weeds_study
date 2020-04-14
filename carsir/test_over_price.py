import pytest
import requests


class TestOverPrice:
    @pytest.mark.parametrize(["grade", "price", "over_price"],[
                             ("S", 3 * 10000, 31300),
                             ("S", 5 * 10000, 52100),
                             ("S", int(6.32 * 10000), 65800),
                             ("S", 8 * 10000, 83200),
                             ("S", int(9.12*10000), 94800)]
                             )
    def test_price(self, grade, price, over_price):
        headers = {"token": "68774b2f709c4bb589c2a23ac6dbfae7", "grp": "nba_pc"}
        url = "http://10.7.200.179:7002/api-olympic-admin/workorder/check/test/getCarPrice"
        request_json = {"carLevel": grade, "car300": price}
        r = requests.post(headers=headers,url=url, json=request_json).json()["data"]
        assert r == over_price
    def test_over(self):
        url = "http://10.7.200.179:7002/api-olympic-admin"
        request_json = {"carLevel": "S", "car300": 30000}
        r = requests.post(url=url,json=request_json)
        print(r.json())
