
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
orderby=driver.find_element(By.NAME,"orderby")
orderby.click()
myoption=driver.find_element(By.CSS_SELECTOR,"#main > div:nth-child(2) > form > select > option:nth-child(5)")
myoption.click()
time.sleep(3)