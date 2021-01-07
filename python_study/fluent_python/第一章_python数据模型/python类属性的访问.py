"""
__getattr __(self,name)
定义当用户试图获取一个不存在的属性时的行为
__getattribute __(self,name)
定义当该类的属性被访问的行为
__setattr __(self,name,value)
定义当一个属性被设置的行为
__delattr __(self,name)
定义当一个属性被删除时的行为
"""


class C:
    def __getattribute__(slef, name):
        print('getattribute')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print('getattr')

    def __setattr__(self, name, value):
        print('setattr')
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(name)


if __name__ == '__main__':
    a = C()
    a.x
    a.x = 1
    del a.x
