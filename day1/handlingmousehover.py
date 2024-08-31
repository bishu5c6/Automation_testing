import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

#deltatime by using these module we can pick or select the next date

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Datepicker.html')
time.sleep(3)

actions = ActionChains(driver)
hover_element = driver.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
time.sleep(4)
actions.move_to_element(hover_element).perform()

driver.find_element(By.CSS_SELECTOR,"a[href='Frames.html']").click()
time.sleep(4)