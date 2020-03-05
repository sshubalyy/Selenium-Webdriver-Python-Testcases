from selenium import webdriver
import time

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("http://amazon.com")

#Capture all tech cookies created by browse
cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies have been created
print(cookies) #print all the cookie pairs

#Adding new cookie to the browser
cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies have been created
print(cookies) #print all the cookie pairs

#Deleting cookies
driver.delete_cookie('Mycookie')
time.sleep(3)
cookies=driver.get_cookies() #capture all cookies
print(len(cookies)) #print size of cookies

driver.delete_all_cookies() #delete all cookies
cookies=driver.get_cookies() #captire all the cookies after delete all
print(len(cookies)) #0
