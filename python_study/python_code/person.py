#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: person.py
@time: 2020/07/16
@remark：
面向对象编程

一切皆对象：

类与实例：
类：把具有相同属性和方法的对象，抽象为一类，
实例：将类进行具体化，比如车是类，楼下的跑车就是实例

类与继承：
被继承者称为父类，也称为超类
继承者：称为子类，
子类可以继承父类的属性和方法
父类的私有属性/方法不能被子类继承，也不能被访问。定义类的私有属性/方法:属性/方法前加__。
如果子类有和父类名称一样的方法，则父类的方法就会被覆盖，俗称对父类方法的重写。如果子类想调用父类的方法，使用super().方法名
self介绍：
self只有在类中才有，独立的函数和方法中没有self
定义类中的方法时，必须要有self
self名称不是必须的，将self用a/b任何字符替换都可以
self表示类实例本身，

定义一个person类
    包含属性：姓名/性别/年龄/存款金额
    包含方法：吃/睡/跑/赚钱

定义一个喜剧演员类
    新增方法：搞笑
"""


class Person:
    name = "default"
    gender = "default"
    age = 18
    # 子类及父类的实例都无法访问私有属性，需要访问私有属性时，只能写方法返回该属性
    __money = 10000

    def __init__(self, name, gender, age, money):
        self.name = name
        self.gender = gender
        self.age = age
        self.__money = money

    def get_money(self):
        """获取私有属性的值"""
        return self.__money

    def eat(self):
        print(f"我在吃 {self.name}")

    def sleep(self):
        print("sleep")

    def run(self):
        print("run")

    # 定义私有方法
    def __make_money(self):
        print("make money")

    def set_name(self, name):
        self.name = name


class FunnyPerson(Person):
    def fun(self):
        print(f"{self.name} is very funny")


class SingerMan(Person):
    # 子类改写父类的方法，self表示类实例本身，可以用其他字符替换
    def eat(self, food):
        print(f"{self.name} eat {food}")

    def run(self, sleep):
        if sleep:
            print("i am sleep,disable run")
        else:
            # 子类调用父类的方法，需要使用super()
            super().eat()

    # 静态方法可以直接调用，不用实例化
    @classmethod
    def song(cls):
        print("sing song")

# 类直接调用静态方法，无需实例化
SingerMan.song()
singer = SingerMan("gaogao", "male", 20, 10000)
singer.eat("meat")
singer.run(False)

# p = Person("dou", "male", 10, 100000)
# # 访问私有方法和属性，python不建议这样做
# p._Person__make_money()
# print(p._Person__money)
# print(dir(p))
#
# f = FunnyPerson("st", "male", 18, 100000)
#
