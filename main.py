from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

from robo_oi import driver as dr

# EXECUTA O PROGRAMA DE ACESSAR O LOGIN 
def abre_site_oi():
    data = datetime.now()
    print(f'iniciando o teste automatizado\nData:{data}')

    login = 'esse@esse.com'
    senha = 1234
    
    dr.entra_site_oi(login,senha)
   



# INTANCIA A FUNCÃO ABRE_SITE_OI
abre_site_oi()