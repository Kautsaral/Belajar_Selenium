from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://thinkjubilee.com/")

#nampilin pop up
#driver.execute_script("alert('Halo dunia')") 

#buka tambaru
driver.execute_script("window.open('https://www.selenium.dev/')")

time.sleep(10)