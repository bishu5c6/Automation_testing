import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker')

driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']").click()
#no we will switch to the frame
frame = driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(frame)
time.sleep(7)
driver.find_element(By.CSS_SELECTOR,"#datepicker").click()
current_date = datetime.now()
# next_date = current_date + timedelta(days=1)
next_date = current_date + timedelta(days=0)

formatted_date = next_date.strftime("%m/%d/%y")

# driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date + Keys.TAB)
driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(5)
driver.quit()