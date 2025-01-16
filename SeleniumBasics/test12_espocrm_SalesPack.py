from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("espocrm Sales Pack Testcase")
@allure.description("TC3 -  Sales Pack ")
@pytest.mark.link
def test_espocrm_salespack():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    login=driver.find_element(By.PARTIAL_LINK_TEXT,"Sales")
    login.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url=="https://www.espocrm.com/extensions/sales-pack/"
    print("Second window title = " + driver.title)
    print(driver.window_handles)