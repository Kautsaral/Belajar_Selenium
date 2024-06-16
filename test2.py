from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://thinkjubilee.com/")
time.sleep(10)
driver.find_element(By.LINK_TEXT, "Jubilee Enterprise Official Site").click() # test click link
time.sleep(10)