from selenium import webdriver


class TestData:
    """
    使用selenium获取网站的性能指标
    """
    def test_data(self):
        driver = webdriver.Chrome()
        driver.get("https://home.testing-studio.com/")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))