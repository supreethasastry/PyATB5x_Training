

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("https://www.amazon.com")

# Maximize browser window (optional)
driver.maximize_window()

# Locate and click on the "Sign-In" button
sign_in_button = driver.find_element(By.CLASS_NAME, "a-button-text")  # Locate the element by ID
sign_in_button.click()

# Pause to view the page (optional)
input("Press Enter to close the browser...")

# Close the browser
driver.quit()