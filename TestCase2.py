import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com.ua")
        print("Title of the page is :" +self.driver.title)
        self.driver.close()

    #def test_Bing(self):
        #self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        #self.driver.get("https://www.bing.com")
        #print("Title of the page is :" + self.driver.title)
        #self.drive.close()

if __name__=="__main__":
    unittest.main()


