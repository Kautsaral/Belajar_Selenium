from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)  #sleep bawaan selenium


driver.find_element(By.NAME, "username").send_keys("@ohmyjacket_")
driver.find_element(By.NAME, "password").send_keys("@Omj2022")
driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
time.sleep(10) #sleep bawaan python
