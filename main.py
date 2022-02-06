from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


email = "design.artt@gmail.com"
passw = os.environ.get("PASS_FB")
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
window_fb = driver.window_handles[1]
window_tinder = driver.window_handles[0]
driver.switch_to.window(window_fb)
print(driver.title)
time.sleep(1)
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'pass').send_keys(passw)
driver.find_element(By.ID, 'pass').send_keys(Keys.ENTER)
time.sleep(1)
try:
    driver.find_element(By.CSS_SELECTOR, "div#buttons label#loginbutton input")

except:
    pass
driver.switch_to.window(window_tinder)
element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="q-315288401"]/div/div/div/div/div[3]/button[1]')))

driver.find_element(By.XPATH, '//*[@id="q-315288401"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="q-315288401"]/div/div/div/div/div[3]/button[1]').click()

driver.find_element(By.XPATH, '//*[@id="q1413092675"]/div/div[2]/div/div/div[1]/button').click()
like_path = '//*[@id="q1413092675"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'
dislike_path = '//*[@id="q1413092675"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'
element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, dislike_path)))
choice_b = driver.find_element(By.XPATH, dislike_path)
for i in range(100):

    try:
        choice_b.click()
        print(i)
        time.sleep(2)
    except:
        driver.find_element(By.XPATH, '//*[@id="q-315288401"]/div/div/div[2]/button[2]').click()
        print("AAA")
        time.sleep(2)

