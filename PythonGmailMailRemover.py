from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#physical path to firefox user profile ex: C:/Users/user/AppData/Roaming/Mozilla/Firefox/Profiles/m9qa343.profile

fp = webdriver.FirefoxProfile("C:/Users/user/AppData/Roaming/Mozilla/Firefox/Profiles/m9qwc6j2.a2")
emails = 50

driver = webdriver.Firefox(fp)
sleep(9)
driver.get("https://www.gmail.com")
sleep(9)
for x in range(emails):
    sleep(3)
    elem = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[7]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/div[1]/div/div")
    elem.click()
    sleep(2)
    #try to get email address from mail not delivered error and print it on the console.
    try:
        elem2 = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/a")
        print(elem2.text)
    except:
        try:
            elem2 = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/a")
            print(elem2.text)
        except:
            print(" ")

    sleep(3)
    elem3 = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]/div")
    elem3.click()
driver.close()
