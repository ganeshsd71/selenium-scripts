#assrtIn & assretNotIn

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        list={"python","selenium","java"}
        #self.assertIn("python",list)  #ok
        #self.assertIn("api", list)    #Failure
        #self.assertNotIn("python", list)  #Failure
        self.assertNotIn("API", list)  #ok




if __name__=="__main__":
    unittest.main()


