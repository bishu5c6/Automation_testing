import alert
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
#
# driver= webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://the-internet.herokuapp.com/javascript_alerts')
#
# AllertButton = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
# AllertButton.click()
# #we cannot inspect the dilog box in order to get the content of the text
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# time.sleep(4)
# #alert.accept() #inorder to confirm the dialog box
# alert.dismiss() #Inorder to cancel the dialog box
# time.sleep(5)



# driver= webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://the-internet.herokuapp.com/javascript_alerts')
#
# AllertButton = driver.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
# AllertButton.click()
# #we cannot inspect the dilog box in order to get the content of the text
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# time.sleep(4)
# #alert.accept() #inorder to confirm the dialog box
# alert.dismiss() #Inorder to cancel the dialog box
# time.sleep(5)

#let's work fpr the 3 type
#we are also giving input to the browser
driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')

AllertButton = driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']")
AllertButton.click()
#we cannot inspect the dilog box in order to get the content of the text
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(4)
alert.send_keys("My name is P.Biswanth")
alert.accept() #inorder to confirm the dialog box
# alert.dismiss() #Inorder to cancel the dialog box
time.sleep(5)