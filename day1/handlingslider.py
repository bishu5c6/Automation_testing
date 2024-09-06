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

driver.get("https://the-internet.herokuapp.com/horizontal_slider")

perform = driver.find_element(By.CSS_SELECTOR,"input[value='0']")
actions = ActionChains(driver)
actions.click_and_hold(perform).move_by_offset(100,0).release().perform()
time.sleep(4)
driver.quit()
