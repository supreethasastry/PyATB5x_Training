from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("espocrm Login Testcase")
@allure.description("TC1 -  Login ")
@pytest.mark.login
def test_espocrm_login_chrome():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    login=driver.find_element(By.ID,"btn-login")
    login.click()
    time.sleep(5)
    assert driver.current_url=="https://demo.us.espocrm.com/?l=en_US"
    #driver.back()
    driver.quit()

    #comment


