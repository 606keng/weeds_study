#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: input_and_out.py
@time: 2020/07/12
@remark：输入与输出
"""

# 字面量插值
# 1.格式化插值，使用%
a = 123
print("%d数值" % a)
name = "tom"
print("name is %s" % name)
# 保留小数点后两位
print("%.2f" % 3.12345)

# format插值法
name = "dou"
age = 22
print("name is {},age is {}".format(name, age))  # 对字符串及整型进行插值
person = ["dou", 22]
print("name is {},age is {}".format(*person))  # 对列表进行插值
people = {"name": "dou", "age": 22}
# 大括号中写入key
print("name is {name},age is {age}".format(**people))  # 对字符串及整型进行插值
# f-string方法,python3.6之后才可以这样使用,打括号中不可以加入反斜杠
name = "gao"
print(f"name is {name}")
print(f"name is {name.upper()}")
print(f"name is {1 + 2}")

# 文件读取
"""    
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
"""
f = open("testfile", "rt")
# 读取文件
print(f.read())
# 判断文件是否可读
print(f.readable())
# 打印第一行数据
print(f.readline())
# 打印第二行数据
print(f.readline())
# 以列表格式打印文件数据
print(f.readlines())

# 关闭文件
f.close()

# 使用with open方法打开文件无需关闭文件，程序会自动回收
with open("testfile", "rt") as f:
    print(f.readlines())

import json

info = {
    "name": "dougao",
    "age": "18",
    "info": ["dougao", "song"]
}
#把数据类型转换为字符串，sort_keys为True，按照key的大小进行顺序排列，indent=4，缩进4个空格
data = json.dumps(info,sort_keys=True,indent=4)
print(data)
#将数据类型转换为字符串，并存储在文件中,indent=4，缩进4个空格
json.dump(info,open("info.json","w"),indent=4)

#将字符串转换为json
info = json.loads(data)
print(type(info))
#从文件中读取字符串，并转换为json
info = json.load(open("info.json","r"))
print(info)