from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/iframe')
driver.maximize_window()

TextEditor = driver.find_element(By.XPATH,"//iframe[@id='mce_0_ifr']")
print(TextEditor)
# TextEditor.clear()
# TextEditor.send_keys("This is the text that I wants to send")

# #in case the link present in the browser is not worked use the below command
# driver.switch_to.default_content()
seleniumlink = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
seleniumlink.click()





time.sleep(3)