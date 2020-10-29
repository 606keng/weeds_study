#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 京东.py
@time: 2020/10/20 
"""
#!usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

"""
@author:DOULIHANG
@file: connect_devices.py
@time: 2020/08/26 
"""
import time

import uiautomator2 as u2
def click_create(d):
    try:
        print("")
        d(text="立即抢购").click()
        return True
    except:
        return False

d = u2.connect_wifi("10.7.201.203")  # connect to device
d.implicitly_wait(60.0)


# d(text="京东").click()
# d(text="我的").click()
# d(scrollable=True).scroll.vert()
# sleep(1)
# d(text="我的预约").click()
# d(textContains="茅台").click()
start_time = time.time()
d(text="立即购买").click_gone(maxretry=60)
d(resourceId="com.jd.lib.settlement.feature:id/a09").click_gone(maxretry=10, interval=0.1)

print(int(time.time() - start_time))