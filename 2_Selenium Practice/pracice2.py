from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")
driver.maximize_window()

driver.find_element(By.ID, "site-header-cart").click()

driver.get("http://demostore.supersqa.com/my-account/")
#<nav class="woocommerce-breadcrumb" aria-label="breadcrumbs"><a href="http://demostore.supersqa.com">Home</a><span class="breadcrumb-separator"> / </span>Cart</nav>

username=driver.find_element(By.ID, "username")
username.send_keys("Supreetha")

password= driver.find_element(By.ID, "password")
password.send_keys("supreetha")

driver.find_element(By.NAME, "login").click()
time.sleep(3)
driver.quit()
