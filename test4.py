from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://thinkjubilee.com/")
driver.refresh()
driver.get("https://www.selenium.dev/")

driver.quit()

#refresh and quit