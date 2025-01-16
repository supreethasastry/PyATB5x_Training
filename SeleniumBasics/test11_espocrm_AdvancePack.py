from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("espocrm Advance Pack Testcase")
@allure.description("TC2 -  Advance Pack ")
@pytest.mark.link
def test_espocrm_advancedpack():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    login=driver.find_element(By.LINK_TEXT,"Advanced Pack")
    login.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url=="https://www.espocrm.com/extensions/advanced-pack/"
    print("Second window title = " + driver.title)
    print(driver.window_handles)
    driver.quit()
