from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = ("https://the-internet.herokuapp.com/dropdown")
driver.get(login_url)

#interacting with thw dropdwon
dropdown_element = driver.find_element(By.ID,"dropdown")
select = Select(dropdown_element)
#three different ways to select an item in the fropdown
#select the value by visible text
#select the value by Index
#select the option by using a values

# select.select_by_visible_text("Option 2")

#select.select_by_index(1)

select.select_by_value("2")

option_count = len(select.options)
expected_count = 3
if option_count == expected_count:
    print("apss")
else:
    print("fail")
time.sleep(3)