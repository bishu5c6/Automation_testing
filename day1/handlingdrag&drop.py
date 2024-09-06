#here we will create a program deagging a box to b -box
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)
source_element = driver.find_element(By.ID,"column-a")
destination = driver.find_element(By.ID,"column-b")
actions = ActionChains(driver)
actions.drag_and_drop(source_element,destination).perform()
time.sleep(9)
driver.quit()