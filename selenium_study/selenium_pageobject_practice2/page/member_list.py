from time import sleep

from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice2.page.base import Base


# from selenium_study.selenium_pageobject_practice.page.index import Index


class MemberList(Base):
    def get_member(self):
        # return self.find(By.CSS_SELECTOR,
        #                                  "#member_list td:nth-child(2)").text
        # 找到成员列表中所有的姓名这一列的元素
        elems = self.finds(By.CSS_SELECTOR, "#member_list td:nth-child(2)")
        # 定义空的姓名列表，将所有的姓名添加到arrs中
        arrs = []
        for elem in elems:
            arrs.append(elem.get_attribute("title"))
        return arrs

    def delete_member(self):
        # 获取成员列表中所有行
        members: list = self.finds(By.CSS_SELECTOR, "#member_list tr")
        # 遍历每一行，如果哪一行姓名列为高可乐，则删除这一行
        for i in range(1, len(members) + 1):
            name = self.find(By.CSS_SELECTOR, "#member_list tr:nth-child(%d) td:nth-child(2)" % i).text
            if name == "高可乐":
                self.find(By.CSS_SELECTOR, "#member_list tr:nth-child(%d) td:nth-child(1)" % i).click()
                self.find(By.CSS_SELECTOR, ".js_operationBar_footer a:nth-child(5)").click()
                self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
                break
        self.find(By.ID, 'menu_index').click()
