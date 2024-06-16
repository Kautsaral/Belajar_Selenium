from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.headless = True  #untuk tidak menampilakn jendela browser (masih gagal)

driver = webdriver.Chrome(options=option)

driver.get("https://thinkjubilee.com/")

alamat = driver.current_url
judul = driver.title
panjangjudul = len(judul)

print("Alamat situs {} dan Judul adalah {}, dengan panjang {}" .format(alamat, judul, panjangjudul))