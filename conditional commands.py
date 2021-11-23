import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://app.influble.com/auth/login?_ga=2.217891861.2060545617.1628857907-805406927.1628857907")

user_ele=driver.find_element_by_xpath("/html/body/app-root/layout/empty-layout/div/div/auth-login/div/div[2]/div[1]/form/mat-form-field[1]/div/div[1]/div/input")
print(user_ele.is_displayed())  # returns true/false based of ele,emt status
print(user_ele.is_enabled())  # returns true/false

psw_ele=driver.find_element_by_xpath("/html/body/app-root/layout/empty-layout/div/div/auth-login/div/div[2]/div[1]/form/mat-form-field[2]/div/div[1]/div[1]/input")

print(psw_ele.is_displayed())  # returns true/false based of ele,emt status
print(psw_ele.is_enabled())  # returns true/false

user_ele.send_keys("clientdemo@influble.com")
psw_ele.send_keys("Demo@2021")
check_box=driver.find_element_by_xpath("/html/body/app-root/layout/empty-layout/div/div/auth-login/div/div[2]/div[1]/form/div[1]/mat-checkbox/label/span[1]").click()

time.sleep(6)

driver.find_element_by_xpath("/html/body/app-root/layout/empty-layout/div/div/auth-login/div/div[2]/div[1]/form/button").click()

roundtip_r