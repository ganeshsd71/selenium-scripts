import time

from  selenium import webdriver
from selenium.webdriver import ActionChains



driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

elememnt=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")

actions=ActionChains(driver)

actions.double_click(elememnt).perform()  #double click on the element
time.sleep(6)

driver.quit()