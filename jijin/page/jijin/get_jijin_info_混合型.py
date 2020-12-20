#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: my_order_detail.py
@time: 2020/08/06
抓取偏股票型基金数据
"""
import os
from time import time, sleep

from selenium.webdriver.common.by import By

from jijin.page.jijin.get_info import get_money_info, get_rask_info, get_craete_time
from jijin.page.web import Web
from jijin.utils.db_operation import DB, DbOperation


class GetInfo(Web):
    def scroll_find(self, value):
        a = True
        print(value)
        i = 0
        while a:
            try:
                i += 1
                if i > 1:
                    return ["豆立航"]
                self._driver.find_element_by_xpath(f"{value}")
                a = False
                element = self._driver.find_element_by_xpath(value)
                try:
                    element.get_attribute('href')
                    return element.text, element.get_attribute('href')
                except:
                    return element.text
            except:
                self.scroll(200)

    def get_list_info(self):
        """
        审批通过车辆入位工单
        :param price:
        :return:
        """
        data = {
            "host": "127.0.0.1",
            "user": "root",
            "password": "dlh480746",
            "database": "jijin"
        }
        db = DbOperation(**data)
        for i in range(0, 41):
            self.scroll(10000)
            ele1 = self._driver.find_element_by_xpath('//*[@id="pnum"]')
            ele1.send_keys(i + 1)
            self._driver.find_element_by_xpath('//*[@id="pgo_41"]').click()
            sleep(3)
            ids = "tblite_hh"
            num = len(self._driver.find_elements_by_xpath(f'//*[@id="{ids}"]/tbody/tr/td[2]/a'))
            for i in range(num):
                jijin_info = {}
                ele = self._driver.find_elements_by_xpath(f'//*[@id="{ids}"]/tbody/tr/td[2]/a')[i]
                jijin_info["name"] = ele.text
                jijin_info["number"] = self._driver.find_elements_by_xpath(f'//*[@id="{ids}"]/tbody/tr/td[1]')[
                    i].text
                ele.click()
                self.switch_window(1)
                account_money = self.scroll_find('//div[2]/table/tbody/tr[1]/td[2]')[0]
                jijin_info["account_money"] = get_money_info(account_money)
                jijin_info['type'] = self.scroll_find('//table/tbody/tr[1]/td[1]/a')[0]
                risk_grade = \
                    self.scroll_find('//div[1]/div[2]/table/tbody/tr[1]/td[1]')[0]
                jijin_info['risk_grade'] = get_rask_info(risk_grade)
                create_time = \
                    self.scroll_find('//div[1]/div[2]/table/tbody/tr[2]/td[1]')[0]
                jijin_info['create_time'] = get_craete_time(create_time)
                jijin_info['manager'] = self.scroll_find('//div[2]/table/tbody/tr[1]/td[3]/a')[0]
                jijin_info['manager_link'] = self.scroll_find('//div[2]/table/tbody/tr[1]/td[3]/a')[1]
                jijin_info['company'] = self.scroll_find('//div[2]/table/tbody/tr[2]/td[2]/a')[0]
                jijin_info['company_link'] = self.scroll_find('//div[2]/table/tbody/tr[2]/td[2]/a')[1]
                jijin_info['last_month_add'] = self.scroll_find('//div[1]/div[1]/dl[1]/dd[2]/span[2]')[0]
                jijin_info['three_month_add'] = self.scroll_find('//div[1]/div[1]/dl[2]/dd[2]/span[2]')[0]
                jijin_info['six_month_add'] = self.scroll_find('//div[1]/div[1]/dl[3]/dd[2]/span[2]')[0]
                jijin_info['last_year_add'] = self.scroll_find('//div[1]/div[1]/dl[1]/dd[3]/span[2]')[0]
                jijin_info['three_year_add'] = self.scroll_find('//div[1]/div[1]/dl[2]/dd[3]/span[2]')[0]
                jijin_info['create_add'] = self.scroll_find('//div[1]/div[1]/dl[3]/dd[3]/span[2]')[0]
                jijin_info['last_week_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[2]/h3')[0]
                jijin_info['last_month_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[3]/h3')[0]
                jijin_info['three_month_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[4]/h3')[0]
                jijin_info['six_month_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[5]/h3')[0]
                jijin_info['this_year_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[6]/h3')[0]
                jijin_info['last_year_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[7]/h3')[0]
                jijin_info['two_year_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[8]/h3')[0]
                jijin_info['three_year_rarking'] = \
                    self.scroll_find('//*[@id="increaseAmount_stage"]//td[9]/h3')[0]
                print(jijin_info)
                sql = f"INSERT INTO `jijin`.`zhishu_jijin`(`name`, " \
                      f"`number`, `account_money`, `type`, `create_time`," \
                      f" `manager`, `manager_link`, `company`, `company_link`," \
                      f" `last_month_add`, `three_month_add`, `six_month_add`, " \
                      f"`last_year_add`, `three_year_add`, `create_add`, " \
                      f"`last_week_rarking`, `last_month_rarking`, " \
                      f"`three_month_rarking`, `six_month_rarking`, " \
                      f"`this_year_rarking`, `last_year_rarking`," \
                      f" `two_year_rarking`, `three_year_rarking`) VALUES ('{jijin_info['name']}', " \
                      f"'{jijin_info['number']}', '{jijin_info['account_money']}', " \
                      f"'{jijin_info['type']}', '{jijin_info['create_time']}', '{jijin_info['manager']}', " \
                      f"'{jijin_info['manager_link']}'" \
                      f", '{jijin_info['company']}', '{jijin_info['company_link']}', '{jijin_info['last_month_add']}'," \
                      f" '{jijin_info['three_month_add']}'," \
                      f" '{jijin_info['six_month_add']}'," \
                      f" '{jijin_info['last_year_add']}', '{jijin_info['three_year_add']}', '{jijin_info['create_add']}'," \
                      f" '{jijin_info['last_week_rarking']}', '{jijin_info['last_month_rarking']}'," \
                      f" '{jijin_info['three_month_rarking']}'," \
                      f"' {jijin_info['six_month_rarking']}'," \
                      f" '{jijin_info['this_year_rarking']}', '{jijin_info['last_year_rarking']}', " \
                      f"'{jijin_info['two_year_rarking']}', '{jijin_info['three_year_rarking']}');"
                print(sql)
                db.insert(sql)
                self.close()
                self.switch_window()
            self.scroll(0)
            sleep(2)


if __name__ == '__main__':
    page = GetInfo().start()
    page.get_list_info()
