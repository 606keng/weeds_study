from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.ID, "kw").send_keys("doulihang")
driver.find_element(By.ID, 'su').click()