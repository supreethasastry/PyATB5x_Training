from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
driver.maximize_window()
# Open Amazon
driver.get("http://demostore.supersqa.com/")
# Pause to view the page (optional)
input("Press Enter to close the browser...")

driver.find_elements(self,by)

# Close the browser
driver.quit()