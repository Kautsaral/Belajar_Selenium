from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert #untuk class alert
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://demoqa.com/alerts")

#driver.find_element(By.ID,"alertButton").click() #untuk tombol alert
#time.sleep(10)

#driver.find_element(By.ID,"confirmButton").click() #menggunakan dissmiss
#time.sleep(10)

driver.find_element(By.ID, "promtButton").click()
time.sleep(10)

#alert = Alert(driver) #untuk tombol alert
#alert.accept()

#alert = Alert(driver) #menggunakan dissmiss
#alert.dismiss()

alert = Alert(driver)
alert.send_keys("kausar")
time.sleep(10)
alert.accept()
time.sleep(10)