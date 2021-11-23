import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")

driver.implicitly_wait(6)

driver.maximize_window()

driver.get("https://www.redbus.in/")

#driver.find_element(By.ID,"redBus Bus Hire").click()


driver.find_element_by_id("redBus").click()     #bus tickets button

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div[1]/input[1]").send_keys("Belgaum") #origin

time.sleep(6)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div[2]/input[1]").send_keys("Mumbai (All Locations)") #destination

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div[3]/input").send_keys("17-Aug-2021")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/button").click()

#Explicit waits
wait=WebDriverWait(driver,10)

element=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/section/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/ul[2]/li[1]/label[1]"))

element.click()

time.sleep(3)

driver.quit()

