from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice2.page.add_member import AddMember
from selenium_study.selenium_pageobject_practice2.page.base import Base


class Index(Base):
    # 实例化该类后，浏览器跳转到https://work.weixin.qq.com/wework_admin/frame页面
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    # 点击添加成员，跳转到添加成员页面
    def goto_add_member(self):
        self.find(By.ID, 'menu_contacts').click()
        # 显式等待，如果添加成员元素出现，则点击该元素
        def wait(driver):
            ele_len = len(self.finds(By.ID, 'username'))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            return ele_len >= 1

        self.wait_for(wait)
        #跳转到添加成员页面
        return AddMember(reuse=True)
