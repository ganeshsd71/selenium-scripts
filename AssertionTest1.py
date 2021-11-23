import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage=driver.title
        #AssertEqual
        #self.assertEqual("Google11",titleOfWebPage,"webpage title are not same")
        self.assertNotEqual("Google",titleOfWebPage,)

if __name__=="__main__":
    unittest.main()