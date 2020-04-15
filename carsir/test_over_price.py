import pytest
import requests


class TestOverPrice:
    @pytest.mark.parametrize(["grade", "price", "over_price"], [
        ("S", int(2.99 * 10000), "车辆暂不符合准入标准"),
        ("S", 3 * 10000, 31300),
        ("S", 5 * 10000, 52100),
        ("S", int(6.32 * 10000), 65800),
        ("S", 8 * 10000, 83200),
        ("S", int(9.12 * 10000), 94800),
        ("S", int(13 * 10000), 134600),
        ("S", int(17.89 * 10000), 185300),
        ("S", int(21 * 10000), 216900),
        ("S", int(31.15 * 10000), 321700),
        ("S", int(34 * 10000), 350200),
        ("S", int(49.99 * 10000), 514800),
        ("S", int(50 * 10000), "车辆暂不符合准入标准"),
        ("S", int(50.01 * 10000), "车辆暂不符合准入标准"),
        ("S", int(100 * 10000), "车辆暂不符合准入标准"),
            ]
                             )
    def test_s_price(self, grade, price, over_price):
        headers = {"token": "68774b2f709c4bb589c2a23ac6dbfae7", "grp": "nba_pc"}
        url = "http://10.7.200.179:7002/api-olympic-admin/workorder/check/test/getCarPrice"
        request_json = {"carLevel": grade, "car300": price}
        r = requests.post(headers=headers, url=url, json=request_json).json()
        if price < 30000 or price>=500000:
            assert r["message"] == over_price
        else:
            assert r["data"] == over_price
    @pytest.mark.parametrize(["grade", "price", "over_price"], [
        ("A", int(2.99 * 10000), "车辆暂不符合准入标准"),
        ("A", 3 * 10000, 30800),
        ("A", 5 * 10000, 51300),
        ("A", int(6.32 * 10000), 64800),
        ("A", 8 * 10000, 82000),
        ("A", int(9.12 * 10000), 93400),
        ("A", int(13 * 10000), 132900),
        ("A", int(17.89 * 10000), 183000),
        ("A", int(21 * 10000), 214400),
        ("A", int(31.15 * 10000), 318000),
        ("A", int(34 * 10000), 346800),
        ("A", int(49.99 * 10000), 509800),
        ("A", int(50 * 10000), "车辆暂不符合准入标准"),
        ("A", int(50.01 * 10000), "车辆暂不符合准入标准"),
        ("A", int(100 * 10000), "车辆暂不符合准入标准"),
            ]
                             )
    def test_a_price(self, grade, price, over_price):
        headers = {"token": "68774b2f709c4bb589c2a23ac6dbfae7", "grp": "nba_pc"}
        url = "http://10.7.200.179:7002/api-olympic-admin/workorder/check/test/getCarPrice"
        request_json = {"carLevel": grade, "car300": price}
        r = requests.post(headers=headers, url=url, json=request_json).json()
        if price < 30000 or price>=500000:
            assert r["message"] == over_price
        else:
            assert r["data"] == over_price
    @pytest.mark.parametrize(["grade", "price", "over_price"], [
        ("B", int(2.99 * 10000), "车辆暂不符合准入标准"),
        ("B", 3 * 10000, 30000),
        ("B", 5 * 10000, 50000),
        ("B", int(6.32 * 10000), 63200),
        ("B", 8 * 10000, 80000),
        ("B", 91200, 91200),
        ("B", int(13 * 10000), 130000),
        ("B", int(17.89 * 10000), 178900),
        ("B", int(21 * 10000), 210000),
        ("B", int(31.15 * 10000), 311500),
        ("B", int(49.99 * 10000), 499900),
        ("B", int(50 * 10000), "车辆暂不符合准入标准"),
        ("B", int(50.01 * 10000), "车辆暂不符合准入标准"),
        ("B", int(100 * 10000), "车辆暂不符合准入标准"),
            ]
                             )
    def test_b_price(self, grade, price, over_price):
        headers = {"token": "68774b2f709c4bb589c2a23ac6dbfae7", "grp": "nba_pc"}
        url = "http://10.7.200.179:7002/api-olympic-admin/workorder/check/test/getCarPrice"
        request_json = {"carLevel": grade, "car300": price}
        r = requests.post(headers=headers, url=url, json=request_json).json()
        if price < 30000 or price>=500000:
            assert r["message"] == over_price
        else:
            assert r["data"] == over_price
    # def test_over(self):
    #     url = "http://10.7.200.179:7002/api-olympic-admin"
    #     request_json = {"carLevel": "S", "car300": 30000}
    #     r = requests.post(url=url,json=request_json)
    #     print(r.json())
