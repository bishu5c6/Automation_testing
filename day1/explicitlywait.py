import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from openpyxl import load_workbook
# for login function we are going to pass it through different users

#creating the excel sheet after that load workbook


driver = webdriver.Chrome()

driver.maximize_window()
# driver.get("https://www.saucedemo.com/v1/")

driver.get("https://www.saucedemo.com/v1/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu']").click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='logout_sidebar_link']")))

element.click()
driver.implicitly_wait(10)
driver.quit()