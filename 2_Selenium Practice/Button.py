from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stock.scriptinglogic.in/amol.html")
c=driver.find_element(By.NAME, "submit")
print(c.text)