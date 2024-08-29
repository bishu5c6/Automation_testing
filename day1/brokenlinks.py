import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = ("https://jqueryui.com/")
driver.get(login_url)

all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"total no of links present: {len(all_links)}")


for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken linK: {href}(Status code is: {response.status_code}) ")

driver.quit()
