#Using contains partial
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
driver.find_element(By.XPATH, "//ul[contains(@id,'site-header')]").click()

