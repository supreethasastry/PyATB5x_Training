

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demostore.supersqa.com/")
s=driver.find_element(By.ID, "woocommerce-product-search-field-0")
s.send_keys('Cap')
s.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()