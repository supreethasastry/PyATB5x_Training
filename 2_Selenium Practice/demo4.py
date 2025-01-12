
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("https://www.amazon.com")

# Maximize browser window
driver.maximize_window()

# Wait and click on the "Sign-In" button
sign_in_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "nav-link-accountList"))
)
sign_in_button.click()

# Pause to view the page (optional)
input("Press Enter to close the browser...")

# Close the browser
driver.quit()