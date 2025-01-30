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
from driver_setup import driver  # Importa o driver configurado
import login_acc
import get_usr

def create_acc():
    usr_brute = get_usr.current_usr()

    # Abrir uma página
    driver.get("https://eternaltwin.org/register/username")
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "username")))

    user = driver.find_element(By.NAME, "username").send_keys(usr_brute + Keys.RETURN)

    user = driver.find_element(By.NAME, "display_name").send_keys(usr_brute + Keys.RETURN)

    user = driver.find_element(By.NAME, "password").send_keys("rasec12345" + Keys.RETURN)

    user = driver.find_element(By.NAME, "password2").send_keys("rasec12345" + Keys.RETURN)

    form = driver.find_element(By.TAG_NAME, "form")
    form.submit()

    driver.get("https://brute.eternaltwin.org/")
    #driver.close()

