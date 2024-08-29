from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = ("https://the-internet.herokuapp.com/dropdown")
driver.get(login_url)

dropdown_element = driver.find_element(By.ID,"dropdown")
target_value = "Option 2"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")
time.sleep(3)

#how to interact with deopdown
#how to interact with select class
#how to use three different methods
#select by visible text
#select by values
#select by id
