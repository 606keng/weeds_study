from carsir_test.easy_sell.api.login import Login


class TestLogin:
    def test_get_token(self):
        Login().get_carsir_token()