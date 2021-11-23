import Xlutils
from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://learn.supporthives.com/devstuffnow/users/login")
driver.maximize_window()

driver.maximize_window()

path="E:/automation testing/login.xlsx"

rows=Xlutils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username=Xlutils.readData(path,"Sheet1",r,1)
    password=Xlutils.readData(path,"Sheet1",r,2)


    driver.find_element_by_xpath("/html/body/section[4]/div/div/div[1]/div/form/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/section[4]/div/div/div[1]/div/form/div[2]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/section[4]/div/div/div[1]/div/form/div[4]/div/button").click()

    if driver.title=="":
        print("test case passed")
        Xlutils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test failed")
        Xlutils.writeData(path,"Sheet1",r,3,"test failed")

    driver.find_element_by_xpath("/html/body/section[1]/div/nav/div/a[1]/button ]").click()