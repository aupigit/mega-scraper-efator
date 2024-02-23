from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    navegador = webdriver.Chrome()
    navegador.get('https://app.efator.com.br/Account/Logon?ReturnUrl=%2FFator') 
    print(navegador.title)
    
    login = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "Usuario")))
    
    navegador.find_element(By.ID, "Usuario").send_keys("Guilherme@megapreco")
    navegador.find_element(By.ID, "Senha").send_keys("100723")

    navegador.find_element(By.XPATH, "/html/body/div[1]/form[1]/div[3]/div/button[2]").submit()
    print('Login done')

    navegador.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/ul/li[9]/span")
    print('achou sair')
    
    assert("Fatoasdr" in navegador.title)
    
    navegador.
        
except Exception as e:
    print(e)


        
    
    # /html/body/div[1]/header/div/div[1]/ul/li[9]/span