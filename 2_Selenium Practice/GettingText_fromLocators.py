import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
c=driver.find_element(By.LINK_TEXT, "Cart")
print(c.text)
b=driver.find_element(By.PARTIAL_LINK_TEXT, "Built with")
print(b.text)
#0 items is not an 'a' tag hence will not work for partial or link text.