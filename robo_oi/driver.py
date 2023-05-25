from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

# EXECUTA O OS PROCESSOS DE LOGIN E SENHA
def entra_site_oi(login,senha):
    navegador = webdriver.Chrome()
    navegador.get('https://portaloisolucoeshml.oi.com.br/login')
    navegador.refresh()
    print('Entrando no site...')
    sleep(10)
    # insere o login
    
    element = WebDriverWait(navegador, 100,2).until(EC.presence_of_element_located((By.ID, 'usernameinput')))
 
    #elemento = WebDriverWait(navegador,10).until(expected_conditions.presence_of_element_located())
    navegador.find_element(By.ID, 'usernameinput').send_keys(login)
    sleep(2)

    # insere a Senha
    wait = WebDriverWait(navegador, 100,2)
    elemento = wait.until(EC.presence_of_element_located(By.ID, 'passwordinput'))
    navegador.find_element(By.ID, 'passwordinput').send_keys(senha)
    sleep(2)

    # clica em acessar
    navegador.find_element(By.ID, 'loginButtonApp').click()
    print('- Login Realizado')




