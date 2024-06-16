import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://barru.pythonanywhere.com/")

driver.find_element(By.ID,"email").send_keys("anakbaru@gmail.com") #test input data ke form
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("test123") #test input data ke form
time.sleep(2)
button = driver.find_element(By.ID,"signin_login") #test click button by ID
button.click()
time.sleep(20)


