import time
import request_my
import get_usr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from driver_setup import driver  # Importa o driver configurado

def do_fight():
    usr_brute = get_usr.current_usr()

    for nr in range(1, 4):
        name_brute = usr_brute + str(nr)
        fights = request_my.fights_left(name_brute)

        while fights > 0:

            if request_my.levelup(name_brute):
                break 
            arena_url = driver.get("https://brute.eternaltwin.org/" + name_brute +"/arena")
            WebDriverWait(driver, 100).until(EC.url_changes(arena_url)) # Wait for the fight start
        
            #WebDriverWait(driver, 5).until(
            #    EC.presence_of_element_located(By.XPATH, "//div[@class='MuiBox-root css-165fahg']")
            #)
            #button = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-165fahg']")  # Button Arena
            #button.click()
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "p.MuiTypography-root.MuiTypography-body1.css-kucysq")) #1st Brute
                )
                button_adv = driver.find_element(By.CSS_SELECTOR, "p.MuiTypography-root.MuiTypography-body1.css-kucysq")
                button_adv.click()
            except TimeoutException:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "p.MuiTypography-root.MuiTypography-body1.css-kucysq")) #1st Brute
                )
                button_adv = driver.find_element(By.CSS_SELECTOR, "p.MuiTypography-root.MuiTypography-body1.css-kucysq")
                button_adv.click()
            
            
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//div[text()='Start fight']"))  # Start Fight
                )   
                
                button = driver.find_element(By.XPATH, "//div[text()='Start fight']")  # Start Fight
            except TimeoutException: 
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//h5[text()='Start fight']"))  # Start Fight 
                )
                button = driver.find_element(By.XPATH, "//h5[text()='Start fight']")  # Start Fight 
            
            button.click()


            WebDriverWait(driver, 100).until(EC.url_changes(not arena_url)) # Wait for the fight start
            cell_url = driver.get("https://brute.eternaltwin.org/" + name_brute +"/cell")
            WebDriverWait(driver, 100).until(EC.url_changes(cell_url)) # Wait for the fight start
            fights = request_my.fights_left(name_brute)
            
            #<button class="MuiBox-root css-1i5638y">Level up!</button> #level up button
                  
    driver.get("https://brute.eternaltwin.org/")
