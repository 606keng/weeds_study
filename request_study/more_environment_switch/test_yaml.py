import yaml


def test_yaml():
    env = {
        "default":"test",
        "environment":{
            "dev": "127.0.0.1",
            "test": "198.0.0.2"
        }
    }
    with open("env.yaml", "w") as f:
        #将env写入文件env.yaml中
        yaml.safe_dump(data=env,stream=f)