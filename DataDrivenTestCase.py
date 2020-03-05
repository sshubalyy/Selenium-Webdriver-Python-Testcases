import XLUtils
from selenium import webdriver

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("http://newtours.demoaut.com")
driver.maximize_window()

path="C:\SeleniumTest\Login1.xlsx"

rows=XLUtils.getRowCount(path,'Лист1')

for r in range(2,rows+1):
    username = XLUtils.readData(path, "Лист1", r, 1)
    password = XLUtils.readData(path, "Лист1", r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("test is passed")
        XLUtils.writeData(path, "Лист1", r, 3, "test passed")
    else:
        print("test failed")
        XLUtils.writeData(path, "Лист1", r, 3, "test failed")

    driver.find_element_by_link_text("Home").click()



















