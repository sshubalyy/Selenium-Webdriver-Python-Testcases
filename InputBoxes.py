from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("https://fs2.formsite.com/meherpavan/form2/index.html?index.html?1537702596407")

#how to finde how many inputboxes present in the webpage
inputboxes=driver.find_elements(By.CLASS_NAME, 'test_field')
print(len(inputboxes)) #8

#how to get status
status=driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Displayed or not:",status) #true/false

status=driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Enable or not:",status) #true/false

#how to provide value into the text box
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("John")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Smith")
#driver.find_element(By.ID, 'RESULT_TextField-3').send_keys("+380931234567")
driver.find_element_by_id('RESULT_TextField-3').send_keys("+380931234567")
