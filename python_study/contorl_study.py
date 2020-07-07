#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: contorl_study.py
@time: 2020/07/07
@remark：python控制流语句学习
"""
"""#分支流与顺序流，分支流如if，控制流如for"""
a = 0

# 分支流
if a == 0:
    print("a==0")
else:
    print("a!=0")

# 多重分支
if a == 0:
    print("a==0")
elif a == 2:
    print("a==2")
elif a == 3:
    print("a==3")

# 分支嵌套
b = 2
c = 3
if b == 2:
    if c == 3:
        print("a===2,c==3")
    else:
        print("b==2,c!=3")
else:
    print("b!=2")

# 计算1-100的和
num = 0
for i in range(101):
    num += i
print(num)
# 计算1-100中偶数的和，使用分支结构
num1 = 0
for i in range(101):
    if i % 2 == 0:
        num1 += i
print(num1)
# 计算1-100中偶数的和，使用range
num2 = 0
for i in range(0, 101, 2):
    num2 += i
print(num2)

# while else语句练习
data = 0
while data == 0:
    print(data)
    data += 1
else:
    print(f"{data} != 0")

# while简单语句组,while只有一条语句时，该语句可以和while写在同一行
data = 0
while data == 0:
    data += 1
else:
    print(f"{data} != 0")

# break：跳出循环，continue：跳出本次循环,输出结果为0，1，3，4
for i in range(11):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
