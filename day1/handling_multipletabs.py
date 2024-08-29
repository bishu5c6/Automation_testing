from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.selenium.dev/downloads/')
driver.switch_to.new_window()
driver.get('https://playwright.dev/')
no_of_tabs = len(driver.window_handles)
print(no_of_tabs)
print()
tabs_values = driver.window_handles
print(tabs_values)
print()
current_tabs = driver.current_window_handle
print(current_tabs)
print()
driver.find_element(By.CSS_SELECTOR,'.getStarted_Sjon').click()
Firsttab = driver.window_handles[0]#giving the index of the tabs
if current_tabs != Firsttab: #
    driver.switch_to.window(Firsttab) #if the baove two we put comment we can open them in a new window and we got exception errorr
driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()



time.sleep(5)