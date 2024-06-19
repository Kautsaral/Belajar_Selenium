from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

#mengisi form otomatis
driver.find_element(By.ID, "userName").send_keys("alka")
time.sleep(5)

driver.find_element(By.ID, "userEmail").send_keys("alka@gmail.com")
time.sleep(5)

driver.find_element(By.ID, "currentAddress").send_keys("kota tangerang")
time.sleep(5)

driver.find_element(By.ID, "permanentAddress").send_keys("Ciledug")
time.sleep(5)

button = driver.find_element(By.ID,"submit")
button.click()
time.sleep(10)