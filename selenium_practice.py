#this is the practice for Selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time


#OPEN PAGE FOR CITRIX CONNECTION
browser = webdriver.Edge()
browser.get("https://citrixgateway.elavon.com/")
time.sleep(2)
# assert "Python" in browser.title

elem = browser.find_element_by_id("Enter user name")

email = raw_input('Enter your Elavon username: ')

elem.clear()
elem.send_keys(str(email))

elem = browser.find_element_by_id("passwd")

password = getpass.getpass("Enter your password + RSA Token: ") #raw_input('Enter your password: ')

elem.clear()
elem.send_keys(str(password))
elem.send_keys(Keys.RETURN)


#CONVERSION BETWEEN PAGES
time.sleep(10)


#THE SKIP WIZARD USING LINKS
elem = browser.find_element_by_id("skipWizardLink").click()

#CONVERSION INTO MAIN ELAVON CITRIX LOGIN PAGE
time.sleep(5)

#ELAVON CITRIX MAIN LOGIN PAGE
elem = 	browser.find_element_by_id("user")
print('found username')
elem.clear()
elem.send_keys("AJWINDS")

# elem = browser.find_element_by_id("password")
# print('found password')
# elem.clear()
# time.sleep(1)
# elem.send_keys("Lindsey92995&")
# elem.send_keys(Keys.RETURN)

elem = browser.find_element_by_id("btnLogin").click()

#CONVERSION TO ELAVON ICON PAGE
time.sleep(10)

elem = browser.find_element_by_id("idCitrix.MPS.App.XA6.Internet_0020Explorer_002011").click()
# except:
	# print('skipped the skip page this time')


# elem = browser.find_Element_by_id("Log on")

# search = input("Enter search item: ")

# elem.clear()
# elem.send_keys(str(search))
# elem.send_keys(Keys.RETURN)

# browser.quit()