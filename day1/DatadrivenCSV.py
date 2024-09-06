import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# import requests
import time
# from datetime import datetime, timedelta
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.support.select import Select
# from openpyxl import load_workbook
import csv

csv_file  = "automation.csv"
test_data = []
with open(csv_file,  "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_data.append(row)
print(test_data)

for data in test_data:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(4)
    driver.find_element(By.ID,"user-name").send_keys(data['ï»¿username'])
    driver.find_element(By.ID,"password").send_keys(data['password'])
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)
    driver.quit()