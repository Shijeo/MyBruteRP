import request_my
import get_usr
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#btn_login = "//div[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSuccess MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButton-colorSuccess MuiButton-root MuiButton-contained MuiButton-containedSuccess MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButton-colorSuccess css-1y5z60y']"
btn_login = "//button[contains(text(), 'Log in')]"

usr_brute = get_usr.current_usr()

# Config ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://eternaltwin.org/login")

cookies = driver.get_cookies()

time.sleep(1)

# InfoInput 
user = driver.find_element(By.NAME, "login").send_keys(usr_brute + Keys.RETURN)
user = driver.find_element(By.NAME, "password").send_keys("rasec12345" + Keys.RETURN)
botao = driver.find_element(By.CSS_SELECTOR, "input[name='sign_in']")
botao.click()

driver.get("https://brute.eternaltwin.org/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, btn_login)) #Button login Sup Corner
)    

button = driver.find_element(By.XPATH, btn_login)
button.click()


nr = 1
name_brute = "Shtst005" #usr_brute+str(nr)

fights = request_my.fights_left(name_brute)

#WebDriverWait(driver, 5).until(
#    EC.presence_of_element_located(By.XPATH, "//div[@class='MuiBox-root css-165fahg']")
#)
#button = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-165fahg']") #Button Arena
#button.click()


#WebDriverWait(driver, 5).until(
#    EC.presence_of_element_located(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-kucysq")
#    )
#button_adv = driver.find_element(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-kucysq")
#button_adv.click()


#WebDriverWait(driver, 5).until(
#    EC.presence_of_element_located(By.XPATH, "//div[@class='MuiBox-root css-4egbmk']") #Start Fight
#)
#button = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-4egbmk']") #Start Fight
#button.click()


#driver.get("https://brute.eternaltwin.org/"+name_brute)



# Fechar o navegador
driver.quit()
