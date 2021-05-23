# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:06:38 2021

@author: Arthur Chabole
=============================
"""

import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from urllib.request import urlopen

def clicar_nome(driver, nome):
    icone = driver.find_element_by_class_name(nome)
    icone.click()
    return None

def clicar_Xpath(driver, XPATH):
    icone = driver.find_element_by_xpath(XPATH)
    icone.click()
    return None
    

#Entrando no site e roubando o source_code
Site ='http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.html'

#Cominho para o chromeDrive funcionar
PATH = 'C:/Users/arthu/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)

#Acessa o site
driver.get(Site)

try:
    icone = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID,"onetrust-accept-btn-handler"))
    )
    icone.click()
    
    ação = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME,"button"))
        )
    ação.click()
except:
    print('Não consegue, néh ?!')
    
Emp_list = '//*[@id="conteudo-principal"]/div[4]/div[3]/div/div[2]/ul/li[2]/a/div/h2'
Letra = 'letra'
Emp = '//*[@id="ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01"]/tbody/tr[1]'
codigo = '//*[@id="accordionDados"]/table/tbody/tr[2]/td[2]/a[2]'

clicar_Xpath(driver, Emp_list)

time.sleep(3)

clicar_nome(driver, Letra)
clicar_Xpath(driver, Emp)

icone = driver.find_element_by_xpath(codigo)

print(icone.text)
