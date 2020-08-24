import requests


class TestHttp:
    def setup(self):
        pass

    def test_request(self):
        r = requests.request(
            'POST',
            url='https://api.carsir.xin/olympic/api-olympic-admin/my/car/listHomeCard',
            data={'orderType': 'QSS', 'carStatus': 'SELLING'},
            cookies={},
            headers={'token': 'dfb5ed89e9e842b7ac225008125d11ef', 'agentid': 'ec0e7ff99bff45d3b9ee4f82e451098a',
                     'version': '20191115', 'grp': 'carsir_app', 'content-type': 'application/json; charset=utf-8',
                     'content-length': '41', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/3.12.1'},
        )
        assert r.status_code == 200
