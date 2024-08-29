from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
# time.sleep(4)
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

#writing code for clicking all the checkboxes
for i in checkboxes:
    i.send_keys(Keys.SPACE)
    time.sleep(2)

#no of checkboxes available in the page

checked_count = 0

for i in checkboxes:
    if i.is_selected():
        checked_count+=1

expected_checked_count = 7
if checked_count == expected_checked_count:
    print("your condition satisfied")
else:
    print("condiyion failed")
time.sleep(5)
driver.close()