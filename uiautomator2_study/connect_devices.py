#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: connect_devices.py
@time: 2020/08/26 
"""
import time

import uiautomator2 as u2

start_time = time.time()
d = u2.connect_wifi("10.7.201.203")  # connect to device
screen = d.info
d.screen_on()

d.swipe_ext("up")
d(resourceId="com.android.systemui:id/key1").click()
d(resourceId="com.android.systemui:id/key2").click()
d(resourceId="com.android.systemui:id/key3").click()
d(resourceId="com.android.systemui:id/key4").click()
d(resourceId="com.android.systemui:id/key5").click()
d(resourceId="com.android.systemui:id/key6").click()

d(text="CarSir").click()

d(resourceId="com.consumer.carsir:id/edt").click()
d.send_keys("16033333333", clear=True)
d(resourceId="com.consumer.carsir:id/btn").click()
d(resourceId="com.consumer.carsir:id/verificationCode").click()
d.send_keys("111111", clear=True)
d(resourceId="com.consumer.carsir:id/tv_easy_show").click()
d(resourceId="com.consumer.carsir:id/city").click()
d.xpath('//*[@resource-id="com.consumer.carsir:id/rv"]/android.widget.LinearLayout[3]').click()
d(resourceId="com.consumer.carsir:id/brand").click()
d.xpath(
    '//*[@resource-id="com.consumer.carsir:id/rv"]/android.widget.LinearLayout[8]/android.widget.LinearLayout[1]').click()
d(resourceId="com.consumer.carsir:id/tv_text").click()
d(resourceId="com.consumer.carsir:id/tv_text").click()
d(resourceId="com.consumer.carsir:id/submit").click()
print(int(time.time() - start_time))