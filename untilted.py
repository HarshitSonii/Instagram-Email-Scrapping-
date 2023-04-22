from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys("username5122001")
password.clear()
password.send_keys("Password")
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

keyword = "#influencer","#indian"
searchbox.send_keys(keyword)

time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
driver.execute_script("window.scrollTo(1000, 2000);")
email = driver.find_elements_by_tag_name('@gmail.com')
email = [email.get_attribute('@gmail.com') for email in emails]
email = email[:-2]

print('Number of scraped emails: ', len(emails))
import os
import wget
path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")
os.mkdir(path)
path
counter = 0
for email in emails:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.csv')
    wget.download(emails, save_as)
    counter += 1
