from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver_path = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"
s = Service(driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com")
driver.maximize_window()
time.sleep(1)
login_b = driver.find_element(By.CSS_SELECTOR, "div a.button span")
login_b.click()
time.sleep(1)
# login_google = driver.find_element(By.XPATH, '//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
login_google = driver.find_element(By.XPATH, '//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/div[2]/button')
print(login_google.text)
login_google.click()
time.sleep(2)
window = driver.window_handles[1]
driver.switch_to.window(window)
print(driver.title)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("ksetty12")
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
