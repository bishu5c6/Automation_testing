from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/nested_frames')
#switching to top frame
driver.switch_to.frame("frame-top")

#switching to middle frame
driver.switch_to.frame("frame-middle")
content = driver.find_element(By.ID,"content").text
print("content in the middle frame: ", content)

#switcj to default conetnt
driver.switch_to.default_content()

#switch to bottom frame
driver.switch_to.frame("frame-bottom")
#content in the bottom
content_bottom = driver.find_element(By.TAG_NAME,"body").text
print("content in the bottom frame: ", content_bottom)

time.sleep(4)