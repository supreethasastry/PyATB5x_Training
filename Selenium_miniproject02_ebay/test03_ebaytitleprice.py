# Open the Url - www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get all the prices
# Print all the titles and prices in the end.
#------------------------------------------------------
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("scrape on ebay site for Mac mini")
@allure.description("TC1 - Positive TC - display the item name and price are scarped successfully")
@pytest.mark.Positive
def test_Get_title_price():
    driver =webdriver.Edge()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    #print("Title of the webpage:",driver.title)
    time.sleep(5)
    #select the search and send "MacMini"
    search_input = driver.find_element(By.XPATH,"//div[@id='gh-ac-wrap']/input")
    search_input.send_keys("Macmini")
    #click on search
    search_button= driver.find_element(By.ID,"gh-search-btn")
    search_button.click()

    # get total number of items in the webpage
    ul_xpath = '//ul[@class="srp-results srp-list clearfix"]'
    ul_element = driver.find_element(By.XPATH, ul_xpath)
    # Find all 'li' elements within the 'ul'
    li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
    # Get the total number of 'li' elements
    total_li = len(li_elements)
    print(f"Total number of 'li' elements: {total_li}")

    for i in range(1,total_li):
        #get xpath for the title of the item
        xpath_1 = f"//ul/li/div/div[2]/a"
        web_element_text = driver.find_element(By.XPATH, xpath_1)
        print(f" item-{i} text:{web_element_text.text}")

        # get xpath for the price of the item
        xpath_2 = f"//ul/li/div/div[2]/div[3]/div/div/span"
        web_element_price = driver.find_element(By.XPATH, xpath_2)
        print(f" item-{i} price:{web_element_price.text}")
    time.sleep(30)
    driver.close()
    # comment