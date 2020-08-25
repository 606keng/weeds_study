#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 多线程.py
@time: 2020/07/13
@remark：python多线程学习
需要后面深入学习：原语/锁/信号量
"""

import logging
from time import ctime, sleep
from _thread import start_new_thread, allocate_lock
import threading

logging.basicConfig(level=logging.INFO)


def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())


def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())


def main():
    """
    使用该方法执行，执行时长为6秒
    :return:
    """
    logging.info("start all at " + ctime())
    loop1()
    loop0()
    logging.info("end all at " + ctime())


def main_thread():
    """
    使用该方法执行，执行时长为4秒
    :return:
    """
    logging.info("start all at " + ctime())
    # _thread主线程退出时，所有的子线程都会被杀掉，所以在线程启动后，要添加sleep
    start_new_thread(loop0, ())
    start_new_thread(loop1, ())
    sleep(4)
    logging.info("end all at " + ctime())


# 使用_thread方法进行多线程操作
loops = [2, 4]


def loop(nloop, nsec, lock):
    """

    :param nloop: 第几次loop
    :param nsec: 等待的秒数
    :param lock: 锁
    :return:
    """
    logging.info(f"start loop{nloop} at {ctime()}")
    sleep(nsec)
    logging.info(f"end loop{nloop} at {ctime()}")
    # 将锁释放
    lock.release()


def main_thread_lock():
    logging.info(f"start all at {ctime()}")
    # 定义锁列表
    locks = []
    # 定义循环次数列表
    nloops = range(len(loops))
    for i in nloops:
        # 定义锁
        lock = allocate_lock()
        # 加锁
        lock.acquire()
        # 将锁加入到锁列表
        locks.append(lock)
        # 为什么不将调用loop函数放在该循环中，因为获取锁需要时间，
        # 如果第二次锁释放的时间晚于第一个锁释放的时间，那么主线程就会退出，导致程序执行结束。
        # 个人感觉不会出现这种情况，主线程的释放，需要两个锁都释放
        # start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        # 启动多线程调用loop
        start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        # 如果锁未被释放，一直循环
        while locks[i].locked():
            pass
    logging.info(f"end all at {ctime()}")


# 使用threading方法进行多线程操作
loops = [2, 4]


def loop_threading(nloop, nsec):
    """

    :param nloop: 第几次loop
    :param nsec: 等待的秒数
    :param lock: 锁
    :return:
    """
    logging.info(f"start loop{nloop} at {ctime()}")
    sleep(nsec)
    logging.info(f"end loop{nloop} at {ctime()}")


def main_threading():
    logging.info(f"start all at {ctime()}")
    # 定义线程列表
    threads = []
    # 定义循环次数列表
    nloops = range(len(loops))
    for i in nloops:
        # 定义线程类
        t = threading.Thread(target=loop_threading, args=(nloops[i], loops[i]))
        # 将线程加入到线程列表中
        threads.append(t)
    for i in nloops:
        # 启动线程
        threads[i].start()
    for i in nloops:
        # 如果锁未被释放，阻塞主线程
        threads[i].join()
    logging.info(f"end all at {ctime()}")


if __name__ == '__main__':
    main_thread()
