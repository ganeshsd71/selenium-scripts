from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://learn.supporthives.com/development-plaza/products")
driver.find_element_by_xpath("/html/body/section[1]/div/nav/ul/ul/li/a[1]/span/img").click()
time.sleep(6)
driver.switch_to_alert().accept() #cleses alert windo using OK button
     #OR
