from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("https://www.amazon.com/")
c=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located(By.LINK_TEXT, "https://web.whatsapp.com/"))
print("Found image")

