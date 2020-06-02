from request_study.api_ddatf.api.wework import WeWrok
class TestWeWork:
    def test_get_token(self):
        secrete = "E1H2f0zNzbTdCzjYBRzXgVs9LeCqGQvLH44VOQm-hFE"
        print(WeWrok().get_token(secrete))