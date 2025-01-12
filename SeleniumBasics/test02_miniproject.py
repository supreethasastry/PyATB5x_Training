import time
from selenium import webdriver
import allure
import pytest

@allure.title("Sample Selenium Prg")

def test_vwo_login():
    driver=webdriver.Edge()
    driver.maximize_window()
    #/instance of browser
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    if "CURA Healthcare Service" in  driver.page_source:
       print("Text found!, Test case Passed")
    else:
       print("Text not found")
       pytest.fail("Text not found!, Test case failed")

    driver.quit()