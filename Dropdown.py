from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get ("https://fs2.formsite.com/meherpavan/form2/index.html?index.html?1537702596407")

#drp=Select(driver.find_element_by_id("RESULT_RadioButton-9")
element=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)

#select by visible text
drp.select_by_visible_text('Morning')  #morning

#select by index
#drp.select_by_index(2) #Afternoon

#select by value
#drp.select_by_value("Radio-2") #evening

#count number of options
print(len(drp.options))

#capture all the options and print them as output

all_options=drp.options

for option in all_options:
    print(option.text)