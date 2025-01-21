from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("ebay Search results test  case")
@allure.description("TC1 -  Capturing Search results ")
@pytest.mark.link
def test_ebaySearch():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(3)
    search_element=driver.find_element(By.XPATH,"//input[@title='Search']")
    search_element.send_keys("Macmini")
    driver.find_element(By.ID,"gh-search-btn").click()
    macmini_title=driver.find_elements(By.XPATH," //div[@class ='s-item__title']")
    total_items=len(macmini_title)
    print(total_items)
    macmini_price = driver.find_elements(By.XPATH, "//span[@class ='s-item__price']")
    for t,p in zip(macmini_title,macmini_price):
      print('title:', t.text)
      print('Price:', p.text)
    total = len(macmini_price)
    print(total)


        #comment
