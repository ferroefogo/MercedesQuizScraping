import browser
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def doQuiz():
    print("---MERCEDES BENZ SCRIPT---")
    frame = browser.find_element_by_xpath('//*[@id="frame"]')
    browser.switch_to.frame(frame)

    time.sleep(2)
    TOS_check = browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/span[1]/div/div[2]/div/div[2]/div[4]/div/label/span[2]")
    TOS_check.click()

    accept_button = browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/span[1]/div/div[2]/div/div[2]/div[4]/button")
    accept_button.click()

        
    
    time.sleep(1)
    play_again = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div[2]/button")
    play_again.click()

    #1.695
    #3.944

    i=7
    time.sleep(1.7)
    for i in range(7):
        time.sleep(4.4)
        q = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/h1")
        q_text = q.text
        
        if q_text == "What is LeBlanc's secondary title?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text
            
            if a1_text == 'The deceiver':
                a1.click()
                i=-1
                
            elif a2_text == 'The deceiver':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                
                
        elif q_text == "Who is the might of Demacia?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Garen':
                a1.click()
                i=-1
                
            elif a2_text == 'Garen':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                
                
        elif q_text == "Which champions are disabled at Worlds 2020?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Samira and Yone':
                a1.click()
                i=-1
                
            elif a2_text == 'Samira and Yone':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champions are disabled at Worlds 2020?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Samira and Yone':
                a1.click()
                i=-1
                
            elif a2_text == 'Samira and Yone':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which team eliminated Albus Nox Luna in 2016?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'H2K':
                a1.click()
                i=-1
                
            elif a2_text == 'H2K':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these players never played at the Worlds stage?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Crownshot':
                a1.click()
                i=-1
                
            elif a2_text == 'Crownshot':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is Lee Sin's secondary title?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'The blind monk':
                a1.click()
                i=-1
                
            elif a2_text == 'The blind monk':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion's ultimate does not have a global range?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Galio':
                a1.click()
                i=-1
                
            elif a2_text == 'Galio':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is the name of the stadium where the games of this year's Worlds will take place?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Pudong Football Stadium':
                a1.click()
                i=-1
                
            elif a2_text == 'Pudong Football Stadium':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the Green Father?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Ivern':
                a1.click()
                i=-1
                
            elif a2_text == 'Ivern':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the boy who shattered time?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Ekko':
                a1.click()
                i=-1
                
            elif a2_text == 'Ekko':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion can't cancel auto attacks?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Kalista':
                a1.click()
                i=-1
                
            elif a2_text == 'Kalista':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "When was Jinx released?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '2013':
                a1.click()
                i=-1
                
            elif a2_text == '2013':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is not an ability of Lee Sin?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'The Show Stopper':
                a1.click()
                i=-1
                
            elif a2_text == 'The Show Stopper':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which team won the most(3) World Championsip titles?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'SK Telecom T1':
                a1.click()
                i=-1
                
            elif a2_text == 'SK Telecom T1':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these abilities is an ultimate?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Lilting Lullaby':
                a1.click()
                i=-1
                
            elif a2_text == 'Lilting Lullaby':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                
                
        elif q_text == "What is Irelia's secondary title?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'The blade dancer':
                a1.click()
                i=-1
                
            elif a2_text == 'The blade dancer':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                





        elif q_text == "How many champions does League of Legends have?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '151':
                a1.click()
                i=-1
                
            elif a2_text == '151':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "Which player got a Pentakill at Worlds 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Viper':
                a1.click()
                i=-1
                
            elif a2_text == 'Viper':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                





        elif q_text == "Worlds 2019 had the most amount of champions picked and banned in the history of Worlds. But do you know how many?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '99':
                a1.click()
                i=-1
                
            elif a2_text == '99':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "The Summoner's Cup is one of the biggest trophies in world sports: Do you know how heavy it is?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "'32kg":
                a1.click()
                i=-1
                
            elif a2_text == "'32kg":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "Who was the 2015 Worlds MVP?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'MaRin':
                a1.click()
                i=-1
                
            elif a2_text == 'MaRin':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "Which city hosted the Worlds 2019 finals?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Paris':
                a1.click()
                i=-1
                
            elif a2_text == 'Paris':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "Which of these teams represent Korea at Worlds 2020?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Gen.G':
                a1.click()
                i=-1
                
            elif a2_text == 'Gen.G':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "Which pair of champions is blood-related?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Katarina and Cassiopeia':
                a1.click()
                i=-1
                
            elif a2_text == 'Katarina and Cassiopeia':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "When does the Baron Nashor spawn for the first time?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '20:00':
                a1.click()
                i=-1
                
            elif a2_text == '20:00':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "Which bonus does the item \"Doran\'s Ring\" not grant?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '+75 Mana':
                a1.click()
                i=-1
                
            elif a2_text == '+75 Mana':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


        elif q_text == "What is the jungle item that grants \"blue smite\" called?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "Stalker's Blade":
                a1.click()
                i=-1
                
            elif a2_text == "Stalker's Blade":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion has the highest health points at level 1?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Tryndamere':
                a1.click()
                i=-1
                
            elif a2_text == 'Tryndamere':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is Nautilus's secondary title?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'The titan of the depths':
                a1.click()
                i=-1
                
            elif a2_text == 'The titan of the depths':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What role plays Lee Sin, the blind monk?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Fighter':
                a1.click()
                i=-1
                
            elif a2_text == 'Fighter':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions has the most World Championship skins?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Thresh':
                a1.click()
                i=-1
                
            elif a2_text == 'Thresh':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these teams never existed?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Samsung Red':
                a1.click()
                i=-1
                
            elif a2_text == 'Samsung Red':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the Sheriff of Piltover?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Caitlyn':
                a1.click()
                i=-1
                
            elif a2_text == 'Caitlyn':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion has to reload after four basic attacks?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Jhin':
                a1.click()
                i=-1
                
            elif a2_text == 'Jhin':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What role plays Irelia, the blade dancer?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Fighter':
                a1.click()
                i=-1
                
            elif a2_text == 'Fighter':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is not an ability of LeBlanc?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Terrashape':
                a1.click()
                i=-1
                
            elif a2_text == 'Terrashape':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the outlaw of Bilgewater?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Graves':
                a1.click()
                i=-1
                
            elif a2_text == 'Graves':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champions critical strike chance is doubled?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Yasuo':
                a1.click()
                i=-1
                
            elif a2_text == 'Yasuo':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champions had the highest win rate at Worlds 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Kennen and Tahm Kench':
                a1.click()
                i=-1
                
            elif a2_text == 'Kennen and Tahm Kench':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these items costs most?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Trinity Force':
                a1.click()
                i=-1
                
            elif a2_text == 'Trinity Force':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which bonus does the item \"Doran\'s Blade\" not grant?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '+3 life on-hit':
                a1.click()
                i=-1
                
            elif a2_text == '+3 life on-hit':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these teams never reached a Worlds semi-final?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Team Liquid':
                a1.click()
                i=-1
                
            elif a2_text == 'Team Liquid':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How many teams participate at Worlds 2020?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '22':
                a1.click()
                i=-1
                
            elif a2_text == '22':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "When does the Herald spawn for the first time?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '08:00':
                a1.click()
                i=-1
                
            elif a2_text == '08:00':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions has the most World Championship skins?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Thresh':
                a1.click()
                i=-1
                
            elif a2_text == 'Thresh':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion can't buy boots?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Cassiopeia':
                a1.click()
                i=-1
                
            elif a2_text == 'Cassiopeia':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "When was Tahm Kench released?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '2015':
                a1.click()
                i=-1
                
            elif a2_text == '2015':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How much base AP does Rabbadon's Deathcap grant?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '120':
                a1.click()
                i=-1
                
            elif a2_text == '120':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which Region hosted the 2015 World Championship?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Europe':
                a1.click()
                i=-1
                
            elif a2_text == 'Europe':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions can generate additional gold with his abilities?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Gangplank':
                a1.click()
                i=-1
                
            elif a2_text == 'Gangplank':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Where did the first League of Legends World Championship take place?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Jönköping':
                a1.click()
                i=-1
                
            elif a2_text == 'Jönköping':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion can't cancel auto attacks?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Kalista':
                a1.click()
                i=-1
                
            elif a2_text == 'Kalista':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion is playable since the beginning?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Ryze':
                a1.click()
                i=-1
                
            elif a2_text == 'Ryze':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "IG vs FPX had the most kills at Worlds 2019. But how many?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '59':
                a1.click()
                i=-1
                
            elif a2_text == '59':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "In which country are League of Legends professionals official athletes?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'USA':
                a1.click()
                i=-1
                
            elif a2_text == 'USA':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these teams represent Europe at Worlds 2020?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Rogue':
                a1.click()
                i=-1
                
            elif a2_text == 'Rogue':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions size does increase with HP?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Zac':
                a1.click()
                i=-1
                
            elif a2_text == 'Zac':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these teams represent North America at Worlds 2020?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Team Liquid':
                a1.click()
                i=-1
                
            elif a2_text == 'Team Liquid':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is not an ability of Ezreal?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Orb of Deception':
                a1.click()
                i=-1
                
            elif a2_text == 'Orb of Deception':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who was the 2014 Worlds MVP?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Mata':
                a1.click()
                i=-1
                
            elif a2_text == 'Mata':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How many players are ranked gold or lower in SoloQ?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '85,5%':
                a1.click()
                i=-1
                
            elif a2_text == '85,5%':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is Ezreal's secondary title?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'The prodigal explorer':
                a1.click()
                i=-1
                
            elif a2_text == 'The prodigal explorer':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these teams never played at the Worlds stage?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Excel Gaming':
                a1.click()
                i=-1
                
            elif a2_text == 'Excel Gaming':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How long was FPX vs. GAM Esports – the shortest game of the Worlds 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '23:33 min':
                a1.click()
                i=-1
                
            elif a2_text == '23:33 min':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which team won Worlds 2012?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Taipei Assasins':
                a1.click()
                i=-1
                
            elif a2_text == 'Taipei Assasins':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is not an ability of Nautilus?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Tremors':
                a1.click()
                i=-1
                
            elif a2_text == 'Tremors':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these Countries never hosted a Worlds game?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Japan':
                a1.click()
                i=-1
                
            elif a2_text == 'Japan':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How many games did it take FPX to win the Worlds 2019 final series?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '3':
                a1.click()
                i=-1
                
            elif a2_text == '3':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which team won Worlds 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'FunPlus Phoenix':
                a1.click()
                i=-1
                
            elif a2_text == 'FunPlus Phoenix':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How many european teams play on the 2020 Worlds main stage?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '3':
                a1.click()
                i=-1
                
            elif a2_text == '3':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions does not have a \"Championship skin\"?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Nidalee':
                a1.click()
                i=-1
                
            elif a2_text == 'Nidalee':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What role plays LeBlanc, the deceiver?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Assassin':
                a1.click()
                i=-1
                
            elif a2_text == 'Assassin':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is not an ability of Irelia?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Bladework':
                a1.click()
                i=-1
                
            elif a2_text == 'Bladework':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What is the release year of League of Legends?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '2009':
                a1.click()
                i=-1
                
            elif a2_text == '2009':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "FPX Crisp was the player with the most assists at Worlds 2019: Do you know how many he had?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '213':
                a1.click()
                i=-1
                
            elif a2_text == '213':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions can teleport nearby allies?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Ryze':
                a1.click()
                i=-1
                
            elif a2_text == 'Ryze':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What do Ezreal, Udyr and Zilean all have in common?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Named after Riot employees':
                a1.click()
                i=-1
                
            elif a2_text == 'Named after Riot employees':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the Loose Cannon?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Jinx':
                a1.click()
                i=-1
                
            elif a2_text == 'Jinx':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which team eliminated SK Telecom T1 in 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'G2':
                a1.click()
                i=-1
                
            elif a2_text == 'G2':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Fnatic vs. OMG (2014) was the longest match ever at Worlds. But how long was it?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '71:34 min':
                a1.click()
                i=-1
                
            elif a2_text == '71:34 min':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the great fire tank of Freljord?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Ornn':
                a1.click()
                i=-1
                
            elif a2_text == 'Ornn':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What's the name of the newest champion?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Samira':
                a1.click()
                i=-1
                
            elif a2_text == 'Samira':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion had the most bans at Worlds 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Pantheon':
                a1.click()
                i=-1
                
            elif a2_text == 'Pantheon':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion has the most skins in League of Legends?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Ezreal':
                a1.click()
                i=-1
                
            elif a2_text == 'Ezreal':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which team was the first Worlds champion in 2011?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Fnatic':
                a1.click()
                i=-1
                
            elif a2_text == 'Fnatic':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Who is the Steel Shadow?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Camille':
                a1.click()
                i=-1
                
            elif a2_text == 'Camille':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "When did Season One World Championship take place?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == '2011':
                a1.click()
                i=-1
                
            elif a2_text == '2011':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which organization has won Worlds the most times?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'SK Telecom T1':
                a1.click()
                i=-1
                
            elif a2_text == 'SK Telecom T1':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champion has the lowest health points at level 1?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Kled':
                a1.click()
                i=-1
                
            elif a2_text == 'Kled':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "What role plays Ezreal, the prodigal explorer?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Marksman':
                a1.click()
                i=-1
                
            elif a2_text == 'Marksman':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which champs ultimate ability is called \"Unstoppable Force\"?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == 'Malphite':
                a1.click()
                i=-1
                
            elif a2_text == 'Malphite':
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                




        elif q_text == "How many fans attended the Worlds 2017 finals in the Beijing National Stadium?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "'40,000":
                a1.click()
                i=-1
                
            elif a2_text == "'40,000":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these champions can put other champions \"asleep\"?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "Zoe":
                a1.click()
                i=-1
                
            elif a2_text == "Zoe":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "FPX LWX was the player with the most kills at Worlds 2019: Do you know how many he had?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "110":
                a1.click()
                i=-1
                
            elif a2_text == "110":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "How many different shoe items exist in League of Legends?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "9":
                a1.click()
                i=-1
                
            elif a2_text == "9":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which of these players has attended Worlds the highest number of times?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "Doublelift":
                a1.click()
                i=-1
                
            elif a2_text == "Doublelift":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                

        elif q_text == "Which was the most played champion at Worlds 2019?":
            a1 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[1]/span")
            a2 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[2]/span")
            a3 = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/span/div/div/div[2]/div/div[3]/span")

            a1_text = a1.text
            a2_text = a2.text
            a3_text = a3.text

            if a1_text == "Kai'Sa":
                a1.click()
                i=-1
                
            elif a2_text == "Kai'Sa":
                a2.click()
                i=-1
                
            else:
                a3.click()
                i=-1
                


def main():
    global browser
    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile

    profile = FirefoxProfile(r'C:\Users\marco\AppData\Roaming\Mozilla\Firefox\Profiles\aiof54fb.default-release')
    browser = webdriver.Firefox(profile)
    browser.get('https://join.stagecast.se/api/web/code/3563//Gs8LNKZKEeREhfjG2Df07SqEonOdwscbjd0Z')
    getMercedes = doQuiz()
    
if __name__=="__main__":
    main()
