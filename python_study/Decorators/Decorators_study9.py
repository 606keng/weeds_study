class Student(object):
    def __init__(self, name):
        self.name = name
        self.name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('输入不合法：年龄必须为数值!')
        if not 0 < value < 100:
            raise ValueError('输入不合法：年龄范围必须0-100')
        self._age=value

    @age.deleter
    def age(self):
        del self._age

xiaoming = Student("小明")

# 设置属性
xiaoming.age = 25

# 查询属性
print(xiaoming.age)

# 删除属性
del xiaoming.age