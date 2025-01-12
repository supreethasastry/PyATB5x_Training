import time
from selenium import webdriver
import allure
import pytest

@allure.title("Espo CRM miniproject")
@allure.description("Verify current url and title of the page")
def test_khatalon_chrome():
        driver = webdriver.Chrome()
        driver.get("https://demo.us.espocrm.com/")
        time.sleep(5)
        print(driver.title)
        print(driver.current_url)
        assert driver.current_url=="https://demo.us.espocrm.com/"
        assert driver.title=="EspoCRM Demo"
