import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com.ua")
        titleOfWebPage=driver.title
        #assertEqual
        #self.assertEqual("Google123",titleOfWebPage,"webpage title is not same")
        self.asserNotEqual("Google",titleOfWebPage)
if __name__ == "__main__":
    unittest.main()