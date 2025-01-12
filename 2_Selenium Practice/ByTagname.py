import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
list = driver.find_element(By.TAG_NAME, "a")
print(list)
list1 = driver.find_element(By.TAG_NAME, "li")
print(list1)
