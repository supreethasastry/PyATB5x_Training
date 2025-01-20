from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.title("opencart register account test case")
@allure.description("TC1 - Verify Your Account is created ")
@pytest.mark.link
def test_opencart_accountcreation():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(3)
    driver.find_element(By.ID,"input-firstname").send_keys("Supreetha")
    driver.find_element(By.ID, "input-lastname").send_keys("Sastry")
    driver.find_element(By.ID, "input-email").send_keys("supreetha2888@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("9999213231")
    driver.find_element(By.ID, "input-password").send_keys("sup9999@")
    driver.find_element(By.ID, "input-confirm").send_keys("sup9999@")
    time.sleep(3)
    driver.find_element(By.XPATH, "// input[ @ name = 'agree']").click()
    driver.find_element(By.XPATH, "// input[ @ value = 'Continue']").click()
    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"
    print(driver.title)
    assert driver.title=="Your Account Has Been Created!"
    # comment



