from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from time import time

timeout=time()+30
five_min=time()+300

service=Service("E:\chrome_driver\chromedriver")
driver=webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
count=driver.find_element(by=By.ID,value="cookie")

# money_ = driver.find_element(by=By.ID, value="money")
# money=int(money_.text)
# money_=driver.find_elements(by=By.CSS_SELECTOR,value="#store div b")
# for i in money_:
#     number=i.text.split()
#     for j in number:
#         new_=number[-1].replace(",","")
#         money_needed=int(new_)

game=True
while game==True:
    count.click()
    if time()>timeout:

        money_ = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        for i in money_:
            number = i.text.split()
            for j in number:
                new_ = number[-1].replace(",", "")
                money_needed = int(new_)

        current_score_ = driver.find_element(by=By.ID, value="money")
        current_score = int(current_score_.text)
        if money_needed==current_score:
            #print("Over")
            break


            #store=driver.find_elements(by=By.ID,value="#store")
#attr=[store.__getattribute__("onclick")]
#for i in attr:
#    i.click()

#time.sleep(30)


driver.quit()

