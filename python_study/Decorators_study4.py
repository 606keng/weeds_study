
"""
装饰器练习-进阶
"""
#3.入门：带参数的函数装饰器

"""
实现功能：
    在装饰器里传入一个参数，指明国籍，并在函数执行前，用自己国家得母语打一个招呼
"""
def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好")
            elif contry == "amercia":
                print("hello")
            else:
                return

            #开始执行函数
            func(*args, **kwargs)
        return deco
    return wrapper

#小明，中国人
@say_hello("china")
def xiaoming():
    pass

#jack。美国人
@say_hello("amercia")
def jack():
    pass

if __name__ == '__main__':
    xiaoming()
