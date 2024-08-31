import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

#deltatime by using these module we can pick or select the next date

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Datepicker.html')
driver.find_element(By.ID,"datepicker2").click()
time.sleep(5)
current_date = datetime.now()
print(f"The current date is: {current_date}")

next_day = current_date + timedelta(days=1)
print()
print(f"the next day date is: {next_day}")
Next_day = (str(next_day.day))
print()
print(f"The next day date is: {Next_day}")
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}"

#handling the dropdowns
Month_dropdown = driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select = Select(Month_dropdown)
select.select_by_value(str(next_month_year))
year_dropdown = driver.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2024")
#selecting the date
driver.find_element(By.LINK_TEXT,Next_day).click()
time.sleep(7)