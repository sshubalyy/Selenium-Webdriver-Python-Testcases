import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com.ua")
        titleOfWebPage=driver.title

        #self.assertTrue(titleOfWebPage == "Google") #True
        self.assertFalse(titleOfWebPage == "Google")
if __name__ == "__main__":
    unittest.main()