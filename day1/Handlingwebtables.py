from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()

driver.get('https://cosmocode.io/automation-practice-webtable/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")#horizontal and vertical values
table = driver.find_element(By.ID,"countries")
rows = table.find_elements(By.TAG_NAME,'tr')
row_count = len(rows)
print(row_count)
#it also counting header row
#to get the exact no of rows use row -1
target_value = "Austria"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME,'td')
    for cell in cells:
        if target_value in cell.text:
            print(f"found values is {target_value}")
            found = True
            break
    if found:
        break
if not found:
    print("Not present in the table")
time.sleep(2)