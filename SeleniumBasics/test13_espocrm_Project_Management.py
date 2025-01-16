from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("espocrm Project Management Testcase")
@allure.description("TC4 -  Project Management ")
@pytest.mark.link
def test_espocrm_project_Manag():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    login=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/extensions/project-management/']")
    login.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url=="https://www.espocrm.com/extensions/project-management/"
    print("Second window title = " + driver.title)
    print(driver.window_handles)