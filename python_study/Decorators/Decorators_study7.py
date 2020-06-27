
"""
装饰器练习-高阶
"""
#7.使用偏函数与类实现装饰器

"""
DelayFunc 是一个实现了 __call__ 的类，delay 返回一个偏函数，在这里 delay 就可以做为一个装饰器
"""
import time
import functools

class DelayFunc:
    def __init__(self, duration, func):
        self.duretion = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Wait for {self.duretion} seconds...")
        time.sleep(self.duretion)
        return self.func(*args, **kwargs)
    def eager_call(self, *args, **kwargs):
        print("Call without delay")
        return self.func(*args, **kwargs)

def delay(duration):
    """
    装饰器：推迟某个函数的执行
    同时提供.eager_call方法立即执行
    :param duration:
    :return:
    """
    return functools.partial(DelayFunc, duration)

@delay(duration=2)
def add(a, b):
    return a+b

if __name__ == '__main__':
    add(5,6)