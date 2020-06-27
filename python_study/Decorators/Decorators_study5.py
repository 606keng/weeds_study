
"""
装饰器练习-进阶
"""
#3.高阶：不带参数的类装饰器

"""
基于类装饰器的实现，必须实现__call__和__init__两个内置函数
    __init__:接收被装饰函数
    __call__：实现装饰逻辑
实现功能：
    实现一个类，不带参数打印日志的装饰器
"""
class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]: the function {func}() is running".format(func = self.func.__name__))
        return self.func(*args, **kwargs)

@logger
def say(something):
    print("say {}!".format(something))

if __name__ == '__main__':
    say("doulihang")