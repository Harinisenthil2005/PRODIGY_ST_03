from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

error = driver.find_element(By.CLASS_NAME, "error-message-container").text

if error:
    print("PASS - Error Message Displayed")
else:
    print("FAIL")

driver.save_screenshot("invalid_login.png")

driver.quit()