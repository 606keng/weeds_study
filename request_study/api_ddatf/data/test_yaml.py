from pprint import pprint

import yaml


def test_load():
    with open("test_tag.yaml",'r') as f:
        pprint(yaml.load(f))