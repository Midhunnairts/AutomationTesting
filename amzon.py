from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def searchAnItem():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#twotabsearchtextbox'))).send_keys('iphone')
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#nav-search-submit-button'))).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'.a-checkbox-fancy').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'.s-color-swatch-inner-circle-fill').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,'#nav-hamburger-menu').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[2]/a').click()
    time.sleep(5)
driver=webdriver.Chrome()
time.sleep(3)
try:
    wait=WebDriverWait(driver,10)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(2)
    searchAnItem()
    

finally:
    driver.quit()


