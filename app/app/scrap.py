from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from prettyconf import config


def login():
    driver = webdriver.Chrome()
    
    driver.get('https://app.efator.com.br/Account/Logon?ReturnUrl=%2FFator')    
 
    username = driver.find_element(By.ID, "Usuario")
    password = driver.find_element(By.ID, "Senha")

    
    username.send_keys(config("EFATOR_USER"))
    password.send_keys(config("EFATOR_PASSWORD"))
    submit = driver.find_element(By.XPATH, "/html/body/div[1]/form[1]/div[3]/div/button[2]")
    submit.click()
    
    
    # /html/body/div[1]/header/div/div[1]/ul/li[9]/span