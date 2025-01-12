from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#//*[@id="main"]/ul/li[2]/a[1]/img
driver.get("http://demostore.supersqa.com/")
driver.implicitly_wait(5)
item=driver.find_element(By.XPATH,"//a[@href='http://demostore.supersqa.com/product/album/']//img[@class='attachment-woocommerce_thumbnail size-woocommerce_thumbnail']")
item.click()
import pdb; pdb.set_trace()
driver.find_element(By.NAME, "add-to-cart").click()

