import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title


        #self.assertTrue(titleOfWebPage == "Google")  #true(OK)
        self.assertTrue(titleOfWebPage == "Google123")  # true(False is not true)
        #self.assertFalse(titleOfWebPage == "Google")  #false ,(True is not false)
        #self.assertFalse(titleOfWebPage == "Google123")  # false ,(OK)



if __name__=="__main__":
    unittest.main()