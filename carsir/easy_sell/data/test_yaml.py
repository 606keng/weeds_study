from pprint import pprint

import yaml


def test_load():
    with open("login.yaml", 'r') as f:
        pprint(yaml.load(f))