from carsir_api.api.login_page.login import Login
class TestLogin:
    def test_get_token(self):
        Login().get_carsir_token()