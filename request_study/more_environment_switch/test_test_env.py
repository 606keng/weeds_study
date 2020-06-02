from request_study.more_environment_switch.test_env import Api


def test_send():
    api = Api()
    data = {
        "method": "get",
        "url": "http://test:9999/demo.txt",
        "headers": None
    }
    print(api.send(data))
