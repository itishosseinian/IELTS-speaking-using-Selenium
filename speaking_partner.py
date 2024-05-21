from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time,random

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)

def prepration():
    driver.get("https://www.bing.com/translator")
    time.sleep(5)

def task1():
    f = open("task1_q.txt",'r')
    task1_q = f.readlines()

    asked = []

    num_asked = 0

    while 1:
        ranq = random.choice(task1_q)

        if ranq in asked:
            continue
        
        if num_asked == 5:
            break

        else:
            input_box = driver.find_element(By.ID,'tta_input_ta')
            input_box.send_keys(ranq)
            time.sleep(4)
            play = driver.find_element(By.ID,'tta_playiconsrc')
            play.click()
            input("Press Enter for Next Question")
            input_box.clear()
            time.sleep(1)
            num_asked+=1
            asked.append(ranq)

def talk(text,wait):
    input_box = driver.find_element(By.ID,'tta_input_ta')
    input_box.send_keys(text)
    time.sleep(4)
    play = driver.find_element(By.ID,'tta_playiconsrc')
    play.click()
    time.sleep(wait)
    input_box.clear()

def task2():
    f = open("task2_q.txt",'r')
    task2_q = f.read()
    task2_q = task2_q.split("#")

    ranq = random.choice(task2_q)

    input_box = driver.find_element(By.ID,'tta_input_ta')
    input_box.send_keys(ranq)
    time.sleep(4)

    play = driver.find_element(By.ID,'tta_playiconsrc')
    play.click()
    print(ranq)
    talk("you have 1 minute to think about it",10)
    time.sleep(60)
    talk("now you can start",7)
    time.sleep(120)
    input("Press Enter ")
    input_box.clear()
    time.sleep(1)
    

if __name__ == "__main__":
    prepration()
    talk("we are in task1, good luck",8)
    task1()
    task2()






    



    