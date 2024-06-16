from selenium import webdriver
import time

driver = webdriver.Chrome()

#driver.maximize_window() #memaksimalkan ukuran window
driver.minimize_window()

driver.get("https://thinkjubilee.com/")

alamat = driver.current_url
judul = driver.title
panjangjudul = len(judul)

print("Alamat situs{} dan Judul adalah{}, dengan panjang{}" .format(alamat, judul, panjangjudul)) #test ambil data current url dan tittle

time.sleep(15)

driver.forward() #untuk maju ke halaman berikutnya
driver.back() #untuk kembali

time.sleep(10)

driver.close()