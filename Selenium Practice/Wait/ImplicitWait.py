from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
driver.find_element(By.ID, "_____").click()
driver.implicitly_wait(10)

