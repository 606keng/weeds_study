"""
装饰器练习
"""
#1.hello，装饰器
"""
装饰器的使用方法
先定义一个装饰器（帽子）
再定义你的业务函数或类（人）
最后把这装饰器（帽子）扣在这个函数（人）头上
"""
def decoretor(func):
    def wrapper(*args, **kwargs):
        print(123)
        return func()
    return wrapper

@decoretor
def function1():
    print("hello, decorator")
"""
装饰器的作用：
    更加优雅，代码结构更加清晰
    将实现特定的功能代码封装成装饰器，提高代码的复用率，增强代码的可读性
"""


if __name__ == '__main__':
    function1()