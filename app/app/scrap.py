from django.shortcuts import render
from prettyconf import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




class Scrapefator:

    def login(self):
        driver = webdriver.Chrome()
        driver.get('https://app.efator.com.br/Account/Logon?ReturnUrl=%2FFator') 
        print(driver.title)
    
        login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Usuario"))
        )
        driver.find_element(By.ID, "Usuario").send_keys(config("EFATOR_USER"))
        driver.find_element(By.ID, "Senha").send_keys(config("EFATOR_PASSWORD"))

        driver.find_element(By.XPATH, "/html/body/div[1]/form[1]/div[3]/div/button[2]").submit()
        print('Login done')

        driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/ul/li[9]/span")
        print('achou sair')
        
    def procura_produto(self, driver, produto):
        driver.find_element(By.ID, "txtPesquisa").send_keys(produto)
        driver.find_element(By.ID, "txtPesquisa").send_keys(Keys.ENTER)
        print('Produto encontrado')
        
    
    # /html/body/div[1]/header/div/div[1]/ul/li[9]/span