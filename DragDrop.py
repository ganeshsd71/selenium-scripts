import time

from  selenium import webdriver
from selenium.webdriver import ActionChains



driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

source_element=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/div/ul/li[1]/img")
target_element=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/div/div")
actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()  #drag and drop
time.sleep(6)

driver.quit()