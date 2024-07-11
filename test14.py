from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()


driver.get("https://www.instagram.com/accounts/login/")


# 1. kita bisa mengatur waktu berdasarkan 2 kondisi, yang pertama durasi dan yang kedua apabila
#kondisi telah ditemukan
#2. kita bisa membuat exception

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
except TimeoutException:
    print("Element tidak ditemukan")


# driver.find_element(By.NAME, "username").send_keys("@ohmyjacket_")
# driver.find_element(By.NAME, "password").send_keys("@Omj2022")
# driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
# time.sleep(10) #sleep bawaan python
