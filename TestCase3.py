import unittest

def setUpModule(): # will be executed before executing any class or any method present in the test class
    print("setUpModule")

def tearDownModule(): #will be executed after completing everything present in the python module
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): # execute before all test methods
        print ("This is login test")

    @classmethod
    def tearDown(self): # execute after all test methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls): #execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls): # execute once when the class started
        print("Close Application")

    def test_search(self): # execute once when the class completed
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaidRecharge test")

if __name__== "__main__":
    unittest.main()


