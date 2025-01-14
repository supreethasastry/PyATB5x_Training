from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.example.com")

element = driver.find_element(By.XPATH,"//button[@id='myButton']")

action_chains = ActionChains(driver)

action_chains.double_click(element).perform()