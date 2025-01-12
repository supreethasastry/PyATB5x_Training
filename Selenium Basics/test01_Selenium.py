import time
from selenium import webdriver
import allure
import pytest

@allure.title("Sample Selenium Prg")
@pytest.mark.regression
def test_vwo_login():
    driver=webdriver.Chrome() #/instance of browser
    driver.get("https://app.vwo.com") #/API request
    print(driver.session_id)
    print(driver.title)
    assert driver.title=="Login - VWO"
    driver.maximize_window()
    time.sleep(10)