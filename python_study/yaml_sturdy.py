#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: yaml_sturdy.py
@time: 2020/07/13
@remark：
"""
import yaml

a = {"name": "doudou", "age": 28}
# 将字典转换为yaml
print(yaml.dump(data=a))
b = [1, 2, 3, 4, "将列表转换为yaml", ]
# 将列表转换为yaml,allow_unicode=True保证中文显示正常
print(yaml.dump(b, allow_unicode=True))
# 将yaml写入到文件中
with open("test.yaml", "w", encoding="utf-8", ) as f:
    f.write(yaml.dump(b, allow_unicode=True))

# 将yaml文件转换为列表，Loader=yaml.FullLoader默认全部载入yaml，不加入该语句，代码会报waring，也可直接使用yaml.sage_load方法
print(yaml.load(open("test.yaml"), Loader=yaml.FullLoader))
print(yaml.safe_load(open("test.yaml")))

