from selenium import webdriver
from selenium.webdriver.common.by import By

# it is used for starting the session
driver = webdriver.Chrome()

#Take action tells which page you want to naviaget
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#give you about the information of the browser
title = driver.title

#implicit time eaiting
driver.implicitly_wait(0.40000)

#finding an element
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#take action element
text_box.send_keys("Selenium")
submit_button.click()

#request element information
message = driver.find_element(by=By.ID, value="message")

#end the session
driver.quit()


