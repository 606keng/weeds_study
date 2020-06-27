
"""
装饰器练习
"""
#3.入门：时间计时器
from time import time, sleep

"""
实现功能：
    计算一个函数的执行时间
"""
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        #执行函数
        func(*args, **kwargs)
        t2 = time()

        #计算执行时长
        cost_time = t2 - t1
        print("花费时间：{}秒".format(cost_time))

    return wrapper

@timer
def wait_sleep(sleep_time):
    sleep(sleep_time)

if __name__ == '__main__':
    wait_sleep(5)