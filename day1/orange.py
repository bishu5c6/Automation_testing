from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
title = driver.title
print(title)
assert "mg" in title