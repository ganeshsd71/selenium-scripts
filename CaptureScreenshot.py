import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

#driver.save_screenshot("E:/automation testing/screenshot/homePage.png")
driver.get_screenshot_as_file("E:/automation testing/screenshot/homePage3.jpg]\")
time.sleep(6)
driver.quit()