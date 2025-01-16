import time
from selenium import webdriver
from selenium.webdriver.common.by  import By
import allure
import pytest

@allure.title("Sample Selenium Prg - multiple browsers")
def test_khatalon_chrome():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(5)
        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
        make_appointement=driver.find_element(By.ID, "btn-make-appointment")
        make_appointement.click()
        time.sleep(5)
        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
        #Comment

