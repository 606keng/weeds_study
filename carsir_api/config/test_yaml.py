from pprint import pprint

import yaml


def test_load():
    with open("env.yaml", 'r') as f:
        pprint(yaml.load(f))