import allure
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType

@allure.title("Checbox, RAdio, Dropdown")
@allure.description("TC1- Verify Checbox. radio and drop down selection")
@allure.feature("Demo of options")
@pytest.mark.positive
def test_checkbox_radio_dropdown():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    r_button=driver.find_element(By.XPATH,"//input[@value='Female']")
    time.sleep(1)
    r_button.click()
    y_exp=driver.find_element(By.XPATH,"//input[@id='exp-4']")
    y_exp.click()
    chbox_1=driver.find_element(By.XPATH,"//input[@id='profession-0']")
    chbox_1.click()
    chbox_2 = driver.find_element(By.XPATH, "//input[@id='profession-1']")
    chbox_2.click()
    time.sleep(1)
    select_tag=driver.find_element(By.ID,"continents")
    select=Select(select_tag)
    select.select_by_visible_text("Europe")
    select.select_by_index(3)
    select_cmd = driver.find_element(By.ID, "selenium_commands")
    select_mul= Select(select_cmd)
    select_mul.select_by_visible_text("Switch Commands")
    select_mul.select_by_index(2)
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="test_verify_checkbox_radio_dropdown-screenshot",
                  attachment_type=AttachmentType.PNG)
