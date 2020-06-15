
"""
装饰器练习-高阶
"""
#8.编写能装饰类的装饰器
from pprint import pprint

"""
编写能装饰类的装饰器
"""
instances = {}

def singleton(cls):
    def get_isntance(*args, **kwargs):
        #cls.__name__获取类名
        cls_name = cls.__name__
        print("=====1=====")
        if not cls_name in instances:
            print("====2====")
            #调用该类
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
            pprint(instances)
        return instances[cls_name]
    return get_isntance

@singleton
class User:
    _instance = None
    def __init__(self, name):
        print("====3====")
        self.name = name

if __name__ == '__main__':
    user = User("doulihang")