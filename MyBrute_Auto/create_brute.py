from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver_setup import driver  # Importa o driver configurado
import get_usr 

def create_brute():
    usr_brute = get_usr.current_usr()
    
    driver.get("https://brute.eternaltwin.org/")
    create_url = driver.current_url

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,  "//button[text()='Log in']"))
        )
        button = driver.find_element(By.XPATH, "//button[text()='Log in']")
        button.click()
    except TimeoutException:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='"+usr_brute+"']"))
        )

    for nr in range(1, 4):    
        name_brute = usr_brute+str(nr)
        campo_input = driver.find_element(By.XPATH, "//input[@type='text' and contains(@class, 'MuiInputBase-input') and @aria-invalid='false']").send_keys(name_brute)
        button = driver.find_element(By.XPATH, "//div[text()='Validate']").click()

        try:
            WebDriverWait(driver, 5).until(EC.url_changes(create_url))
            print(f"Brute {nr} - {name_brute} Criado.")
    
        except TimeoutException:
            print(f"Brute {name_brute} já existe.")    
        
        
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='MuiAlert-message css-1xsto0d' and text()='You have reached your brute limit. You need 500 Gold to unlock a new brute.']"))
            )
        except TimeoutException:
            driver.get(create_url)  
    #driver.close()

