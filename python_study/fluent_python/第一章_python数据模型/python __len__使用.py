#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: python __len__使用.py
@time: 2021/01/07
@remark：
"""
"""
如果一个类表现得像一个list，要获取有多少个元素，就得用 len() 函数。要让 len() 函数工作正常，
类必须提供一个特殊方法__len__()，它返回元素的个数
"""

class Students(object):
    def __init__(self, *args):
        self.names = args

    def __len__(self):
        return len(self.names)


if __name__ == '__main__':
    a = Students("小明", "小豆", "小高")
    print(len(a))
