from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get ("https://www.expedia.com/")

#driver.find_element_by_id("tab-flight-tab-hp").click()

driver.find_element(By.ID,"tab-flight-tab-hp").click() #click on Flights button

time.sleep(2) #from python

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys ("SFO")

time.sleep(2)

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys ("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("12/01/2020")

#driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys(Keys.CONTROL+"a") 
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("15/02/2020")

#driver.find_element_by_class_name("btn-primary btn-action gcw-submit")click()
driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()