from selenium import webdriver

from selenium.webdriver import ActionChains

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("https://swisnl.github.io/jQuery-contextMenu/demo.html")

element=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions=ActionChains(driver)
actions.context_click(element).perform() #mouse right click