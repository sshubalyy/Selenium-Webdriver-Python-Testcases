from selenium import webdriver
#if we want to specify download place
#from selenium.webdriver.chrome.options import Options
#chromeOptions=Options()
#chromeOptions.add_experimental_option("pref,{download.default_directory": "C:\Downloadedfiles"})
driver=webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe"#,chrome_options=chromeOptions)

driver.get ("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#Download text file
driver.find_element_by_id("textbox").send_keys("testing download test file")
driver.find_element_by_id("createTxt").click() #Generate file button
driver.find_element_by_id("link-to-download").click() #Download link

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing download pdf file")
driver.find_element_by_id("createPdf").click() #Generate file button
driver.find_element_by_id("pdf-link-to-download").click() #Download link