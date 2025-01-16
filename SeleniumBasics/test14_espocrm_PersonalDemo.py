from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("espocrm Personal Demo Testcase")
@allure.description("TC5 -  Personal Demo ")
@pytest.mark.link
def test_espocrm_personaldemo():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    login=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']")
    login.click()
    time.sleep(5)
    assert driver.current_url=="https://www.espocrm.com/cloud-registration/?plan=demo"
    #print(driver.window_handles)

    # comment