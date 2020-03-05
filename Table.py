from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("file:///C:/Users/serhi/Downloads/new1.html")

rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")  #count number of rows
cols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")) #count number of columns

print(rows)
print(cols)

print("Product"+"    "+"Article"+"    "+"Price")

for r in rage(2,rows+1):
    for c in range(1,cols+1):
value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
print(value,end='      ') # produc1 0001 10
print ()