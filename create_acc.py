from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('usr_atu.txt', 'r') as arq_usr:
    usr_brute = arq_usr.read()  # Lê todo o conteúdo do arquivo
usr_brute = usr_brute[:-2] + str(int(usr_brute[-2:]) + 1).zfill(2)  # Pega os últimos 2 caracteres, soma 1 e coloca de volta
arq_usr.close()


with open('usr_atu.txt', 'w') as arq_usr:
    arq_usr.write(usr_brute)
arq_usr.close()

with open('usr_brute.txt', 'a') as arq_usr:
    arq_usr.write(usr_brute+";")
arq_usr.close()

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

#time.sleep(5)
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

input("Pressione Enter para fechar o navegador...")
# Fechar o navegador
driver.quit()
