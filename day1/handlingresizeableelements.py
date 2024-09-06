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
driver.get("https://demo.automationtesting.in/Resizable.html")

resizeable_element = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
Initial_element_size = driver.find_element(By.CSS_SELECTOR,"#resizable")
initial_size = Initial_element_size.size
print("Intial_size is: ",initial_size)
time.sleep(5)
action_chains = ActionChains(driver)
action_chains.click_and_hold(resizeable_element).move_by_offset(100,100).release().perform()
time.sleep(5)
resized_element = Initial_element_size.size
print("Resized size is: ",resized_element)
driver.quit()
