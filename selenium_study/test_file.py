from time import sleep

from selenium.webdriver.common.by import By

from selenium_study.base import Base


class File(Base):
    """
    上传文件练习
    """
    base_url = "https://image.baidu.com/"

    def case_file(self):
        self.operation_element((By.CSS_SELECTOR, ".st_camera_off"), "c")
        self.upload_file((By.ID, "stfile"), r'/Users/doulihang/work/project/weeds_study/selenium_study/1.jpg')
        # self.driver.get("https://image.baidu.com/")
        # self.driver.find_element(By.CSS_SELECTOR,".st_camera_off").click()
        # self.driver.find_element_by_id("stfile").send_keys(r"1.jpg")
        sleep(5)


class TestFile:

    def setup(self):
        self.file = File()

    def teardown(self):
        self.file._driver.quit()

    def test_file(self):
        self.file.case_file()
