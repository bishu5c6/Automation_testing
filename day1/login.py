from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()

user_name = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/v1/index.html"
driver.get(login_url)

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(user_name)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, "login-button")
assert not login_button.get_attribute("disabled")
login_button.click()

success_element = driver.find_element(By.CSS_SELECTOR, ".product_label")
assert success_element.text == 'Productss'

# time.sleep(10)
# driver.quit()