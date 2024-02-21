from selenium import webdriver

def scrap(request):
    driver = webdriver.Chrome()
    
    driver.get('https://app.efator.com.br/Account/Logon?ReturnUrl=%2FFator')    
 
    username = driver.find_element_by_id("Usuario")
    password = driver.find_element_by_id("Senha")
    
    