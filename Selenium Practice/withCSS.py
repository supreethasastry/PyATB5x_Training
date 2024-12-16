#site-header-cart > li.current-menu-item > a
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("http://demostore.supersqa.com/")
c=driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
c.click()

m=driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
m.click()
#xpath : //*[@id="site-navigation"]/div[1]/ul/li[4]
time.sleep(3)
driver.quit()

