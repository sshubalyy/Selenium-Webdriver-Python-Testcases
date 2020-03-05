from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("https://fs2.formsite.com/meherpavan/form2/index.html?index.html?1537702596407")

#working with radio buttons

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() #true/false
print(status)

button = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]')
driver.execute_script("arguments[0].click();", button)

status=driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]').is_selected()
print(status)

#working with check boxes

driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click() #monday
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[6]/td/label").click() #friday

status=driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").is_selected() #friday
print(status)
