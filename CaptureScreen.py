from selenium import webdriver

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("http://amazon.com")

#driver.save_screenshot("C:\Screen\amazon.png")
driver.get_screenshot_as_file("C:/Screen/amazon1.png")