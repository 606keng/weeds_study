from time import sleep

from selenium.webdriver.common.by import By

from selenium_study.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,".st_camera_off").click()
        self.driver.find_element_by_id("stfile").send_keys(r"D:\work\auto\weeds_study\selenium_study\1.jpg")
        sleep(5)