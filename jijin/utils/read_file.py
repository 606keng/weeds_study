#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: read_file.py
@time: 2020/06/29 
"""
import json
import os


class ReadFile(object):
    def read_json(self, file, path=os.path.dirname(__file__), old_string=None, new_string=None):
        """
        读取json文件
        """
        data = json.load(open(path + r'/' + file, encoding="utf-8"))
        # 如果new_string、old_string都不为None，则将data中的old_string替换为new_string
        if new_string and old_string:
            # 将json转换为字符串，indent=2每行2个空格缩进，ensure_ascii=False：清除json中中文乱码的问题
            data = json.dumps(data, indent=2, ensure_ascii=False).replace(old_string, new_string)
            return json.loads(data)
        else:
            return data
