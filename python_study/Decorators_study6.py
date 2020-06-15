
"""
装饰器练习-进阶
"""
#3.高阶：带参数的类装饰器

"""
基于类装饰器的实现，必须实现__call__和__init__两个内置函数
    __init__:不再接收被装饰函数，接收传入的参数
    __call__：接收被装饰函数，实现装饰逻辑
实现功能：
    实现一个类，不带参数打印日志的装饰器
"""
class logger(object):
    #接收参数
    def __init__(self, level = "INFO"):
        self.level = level

    #接收函数
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running".format(level=self.level,func = func.__name__))
            func(*args, **kwargs)
        #返回函数
        return wrapper
@logger(level="WARNING")
def say(something):
    print("say {}!".format(something))

if __name__ == '__main__':
    say("doulihang")