from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Firefox (executable_path="C:\Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get ("http://newtours.demoaut.com")

print (driver.title)

print(driver.current_url)

#print (driver.page_source)

driver.close()