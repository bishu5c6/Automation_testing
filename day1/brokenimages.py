from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/broken_images')
driver.maximize_window()
images = driver.find_elements(By.TAG_NAME,'img')
broken_images =[]
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found ")

if broken_images:
    print("list of broken images: ")
    for i in broken_images:
        print(i)
else:
    print("No broken images found: ")
time.sleep(5)
