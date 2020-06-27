"""
装饰器练习
"""
#2.入门：日志打印器
"""
实现功能：
    在执行函数前，打印一行日志，告知主人要执行函数了
    在函数执行完，再打印一行日志告知主人，执行完了
"""
def logger(func):
    def wrapper(*args, **kwargs):
        print("主人，我准备开始执行函数：{}函数了".format(func.__name__))
        #执行函数
        func(*args, **kwargs)
        print("主人，我执行完了")
    return wrapper

@logger
def add(x, y):
    print("{} + {} = {}".format(x, y, x+y))
"""
装饰器的作用：
    更加优雅，代码结构更加清晰
    将实现特定的功能代码封装成装饰器，提高代码的复用率，增强代码的可读性
"""

if __name__ == '__main__':
    add(5, 8)