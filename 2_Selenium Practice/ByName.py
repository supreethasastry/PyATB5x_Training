import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
orderby=driver.find_element(By.NAME,"orderby").click()
time.sleep(3)
print(orderby.text)

