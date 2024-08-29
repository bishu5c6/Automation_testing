from selenium import webdriver
import time

viewports =[(1024,768),(768,1024),(375,667),(414,896)]
#from these array we need to run everytime
driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")

try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(4)
except Exception as e:
    print(e)
finally:
    print("successfully completed the execution")