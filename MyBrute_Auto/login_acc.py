import get_usr
import fight_brute
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from driver_setup import driver  # Importa o driver configurado

def login_acc(): 

    usr_brute = get_usr.current_usr()
    
    
    driver.get("https://eternaltwin.org/login")
    cookies = driver.get_cookies()

    time.sleep(1)

    # Info Input 
    user = driver.find_element(By.NAME, "login").send_keys(usr_brute + Keys.RETURN)
    user = driver.find_element(By.NAME, "password").send_keys("rasec12345" + Keys.RETURN)
    botao = driver.find_element(By.CSS_SELECTOR, "input[name='sign_in']")
    botao.click()

    driver.get("https://brute.eternaltwin.org/")

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Log in')]")) #Button login Sup Corner
        )       
    except TimeoutException:
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Log in')]")) #Button login Sup Corner
        )   

    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    button.click()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='"+usr_brute+"']"))
        )
    except TimeoutException:   
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='"+usr_brute+"']"))
        )

    #driver.close()
