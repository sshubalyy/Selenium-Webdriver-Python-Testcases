from selenium import webdriver
import time

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to_frame("packageListFrame") #first frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to_frame("packageFrame") #second frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to_frame("classFrame") #third frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()