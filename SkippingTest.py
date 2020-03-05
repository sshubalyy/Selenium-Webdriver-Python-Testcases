import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method becouse it isn't yet ready")
    def test_advancedsearch(self):
        print("This is adv search method")

    @unittest.skipIf(1==1,"Numbers are not equals")
    def test_prepaidrecharge(self):
        print("This is pre-paid recharge")

    def test_postpaidcharge(self):
        print("This is postpaid recharge")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("this is login by twitter")

if __name__== "__main__":
    unittest.main