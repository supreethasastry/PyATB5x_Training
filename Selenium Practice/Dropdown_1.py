import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open Amazon
driver.get("http://demostore.supersqa.com")
orderby=driver.find_element(By.NAME,"orderby")
dropdown_object= Select(orderby)
#dropdown_object.select_by_visible_text('Sort by popularity')
#dropdown_object.select_by_index(1)
#dropdown_object.select_by_value("date")
all_options=dropdown_object.options
for option in all_options:
    print(option.text)
time.sleep(3)
