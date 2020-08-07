#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: data_dispose.py
@time: 2020/08/07 
"""
def save_data():
    list = [i for i in range(1000000)]
    list.insert(10000,"A17283")
    for i in list:
        with open("data.txt","a") as f:
            f.write(str(i))

# for i in list:
#     try:
#         int(i)
#     except:
#         print(f"{i}不为纯数字")
# print(len(list))
# print(len(set(list)))

if __name__ == '__main__':
    save_data()