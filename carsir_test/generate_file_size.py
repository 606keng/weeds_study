#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: generate_file_size.py
@time: 2020/07/16 
"""
import string
import sys
import random
def generate_size():
    try:
        file_size = sys.argv[1]
        file_cell = sys.argv[2]
    except:
        print("Usage:\n generate_file_size.py file_size file_cell")
        return
    # print(file_size,file_cell)
    # 得到随机字符
    rand_str = string.ascii_letters
    # 文件名
    file_name = str(file_size) + str(file_cell) + "_file" + ".doc"
    # print(type(file_size),rand_str)
    file_cell = str(file_cell).upper()
    if file_cell and file_size:
        if file_cell == "GB":
            file_size  = float(file_size) * 1024 * 1024 * 1024
        elif file_cell == "MB":
            file_size = float(file_size) * 1024 * 1024
        elif file_cell == "KB":
            file_size = float(file_size) * 1024
        elif file_cell == "B":
            file_size == float(file_size)
        else:
            print("enter cell is not correct")
            return
    else:
        print("Usage:\n generate_file_size.py file_size file_cell")
        return
    print("begin generate file,please waiting for a while")
    if int(str(file_size).split('.')[1]) >= 5:
        file_size = file_size + 1
    print(file_size)
    with open(file_name,"w") as fs:
        for i in range(int(file_size)):
            fs.write(random.choice(rand_str))
    print("generate end, file name is {}".format(file_name))

generate_size()
