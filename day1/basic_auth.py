import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

username = "admin"
password = "admin"
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
#in these you have to change the link add some some changes to the link
#https://username:passwoord@domain/path