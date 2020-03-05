#assertIsNone & asserIsNotNone
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
    #driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver = None
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)
if __name__ == "__main__":
    unittest.main()