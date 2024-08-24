# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# #driver = webdriver.Chrome()
#
# #driver = webdriver.Chrome(executable_path='location of the drivers if it is not present in ')
#
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#
# #enter the user name in the box
# #to find all the elements in the web page
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.ID, "password").send_keys("admin123")
# driver.find_element(By.ID, "submit").click()
#
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print('login is passed')
# else:
#     print('login is failed')
#
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.maximize_window()
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()