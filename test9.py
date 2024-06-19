from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

driver.find_element(By.XPATH,"//*[@id='sex-0']").click() #radiobutton

driver.find_element(By.ID,"profession-0").click() #check box

time.sleep(5)