import time
from selenium import webdriver
import allure
import pytest

@allure.title("Sample Selenium Prg - multiple browsers")
def test_khatalon_chrome():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(5)
        assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"

def test_khatalon_edge():
        driver = webdriver.Edge()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(5)
        assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
