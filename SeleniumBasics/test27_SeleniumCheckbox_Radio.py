import allure
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

@allure.title("Checbox, RAdio, Dropdown")
@allure.description("TC1- Verify Checbox. radio and drop down selection")
def test_checkbox_radio_dropdown():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    r_button=driver.find_element(By.XPATH,"//input[@value='Female']")
    time.sleep(3)
    r_button.click()
    y_exp=driver.find_element(By.XPATH,"//input[@id='exp-4']")
    y_exp.click()
    chbox_1=driver.find_element(By.XPATH,"//input[@id='profession-0']")
    chbox_1.click()
    chbox_2 = driver.find_element(By.XPATH, "//input[@id='profession-1']")
    chbox_2.click()
    time.sleep(3)