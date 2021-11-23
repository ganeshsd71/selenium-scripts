import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "D:\sunil"})

driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe",chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()
#how to download text files


driver.find_element_by_id("textbox").send_keys("Ganesh Dhamnekar testing download files")
driver.find_element_by_id("createTxt").click() #genarate file
driver.find_element_by_id("link-to-download").click()  #download the link

driver.find_element_by_id("pdfbox").send_keys("Ganesh Dhamnekar testing download files")
driver.find_element_by_id("createPdf").click() #genarate file
driver.find_element_by_id("pdf-link-to-download").click()  #download the link pdf

time.sleep(6)

driver.quit()