from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\drivers\chrome driver\chromedriver.exe")
driver.get("https://www.amazon.in/")

#capture all teh coockies created bt browser

coockies=driver.get_cookies()

print(len(coockies)) #print number of coockies have been created


print(coockies) #print all the cookies page

#adding new coolie to the browseer
cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

coockies=driver.get_cookies()
print(len(coockies)) #print number of coockies after adding new cookie
print(coockies) #print all the cookies page

#Deleting cookie
driver.delete_cookie('Mycookie',)
coockies=driver.get_cookies() #capture all the cookies from the browser after deleting cookie
print(len(coockies))  #print number of cookies after deletimg the cookie

#Deleting all the coockies
driver.delete_all_cookies() #deletes all cookie
coockies=driver.get_cookies() #capture all the cookies after deletes all
print(len(coockies)) #0