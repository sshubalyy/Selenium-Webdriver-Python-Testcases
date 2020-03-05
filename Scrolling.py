from selenium import webdriver

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window() #mximize windows size

#1.scroll  down page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#2.scroll down page till the element is visible
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[93]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#3.scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")