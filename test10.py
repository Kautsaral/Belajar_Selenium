from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

menu = Select(driver.find_element(By.ID,"continents")) #mengisi menu select

menu.select_by_visible_text('Australia')
time.sleep(5)