from time import sleep

from selenium.webdriver.common.by import By

from selenium_study.base import Base


class TestFile(Base):
    """
    上传文件练习
    """
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,".st_camera_off").click()
        self.driver.find_element_by_id("stfile").send_keys(r"1.jpg")
        sleep(5)