from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com')

sleep(1)
Id_find = 'APjFqb'
button = driver.find_element(By.ID, Id_find)
button.click()
sleep(1)

def for_delet(message : any):
    this_B = driver.find_element(By.ID ,message)
    this_B.send_keys(Keys.BACKSPACE * 100)


def for_writing(message : any, boto : any):
     for key in message:
          boto.send_keys(key)
          message = ''

def click_on_add(message : any):
    enter_to = driver.find_element(By.ID, message)
    enter_to.send_keys(Keys.ENTER)

string = input("Ok can you please write somthing :")
number = 1
write_flag = 0

while True:
    if (number == 1):
        for_writing(string, button)
        number = 0
        write_flag = 1
    sleep(1)
    if write_flag == 1:
        option = input("Deleting what u write Please Press \n[1] delete \n[2 to enter\n\n :]")
        if (option == '1'):
            for_delet(Id_find)
            check = input("Wanna re write somthing ?? [yes] or [No]")
            if (check == 'yes'):
                string = input("Ok can you please write somthing... ")
                number = 1
            elif(check == 'No'):
                number = 0
        elif (option == '2'):
            click_on_add(Id_find)
            break



result = input("OK Write Exactly the Title U wanna enter ... :")
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, result))
        )
except :
    print("Tooo long ...?")
try:
    link = driver.find_element(By.PARTIAL_LINK_TEXT, result)
    link.click()
except:
    print("Try Again")
input()
driver.quit()