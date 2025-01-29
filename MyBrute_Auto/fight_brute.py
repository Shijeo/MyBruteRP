import request_my
import get_usr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def do_fight():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for nr in range(1, 3):
        name_brute = get_usr.current_usr() + str(nr)
        fights = request_my.fights_left(name_brute)

        while fights > 0:
            
            driver.get("https://brute.eternaltwin.org/" + name_brute)

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(By.XPATH, "//div[@class='MuiBox-root css-165fahg']")
            )
            button = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-165fahg']")  # Button Arena
            button.click()

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-kucysq")
            )
            button_adv = driver.find_element(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-kucysq")
            button_adv.click()

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(By.XPATH, "//div[@class='MuiBox-root css-4egbmk']")  # Start Fight
            )
            button = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-4egbmk']")  # Start Fight
            button.click()

            fights = request_my.fights_left(name_brute)
