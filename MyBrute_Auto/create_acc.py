from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import get_usr

usr_brute = get_usr.current_usr()

get_usr.next_usr()

# Configuração automática do ChromeDriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir uma página
driver.get("https://eternaltwin.org/register/username")

user = driver.find_element(By.NAME, "username").send_keys(usr_brute)

user = driver.find_element(By.NAME, "display_name").send_keys(usr_brute)

user = driver.find_element(By.NAME, "password").send_keys("rasec12345")

user = driver.find_element(By.NAME, "password2").send_keys("rasec12345")

form = driver.find_element(By.TAG_NAME, "form")
form.submit()

driver.get("https://brute.eternaltwin.org/")
button = driver.find_element(By.XPATH, "//button[text()='Log in']")
button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='"+usr_brute+"']"))
)
nr = 1
name_brute = usr_brute+str(nr)
campo_input = driver.find_element(By.XPATH, "//input[@type='text' and contains(@class, 'MuiInputBase-input') and @aria-invalid='false']").send_keys(name_brute)

create_url = driver.current_url

button = driver.find_element(By.XPATH, "//div[text()='Validate']")
button.click()

success_url = driver.current_url


while create_url == success_url:    
    name_brute = usr_brute+str(nr)
    campo_input = driver.find_element(By.XPATH, "//input[@type='text' and contains(@class, 'MuiInputBase-input') and @aria-invalid='false']").send_keys(name_brute)
    button.click()
    nr+=1

# Fechar o navegador
driver.quit()
