# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:42:08 2021

@author: Arthur Chabole
=============================
Este programa acessa o site 'statusinvest' e procura as ações indicadas no vetor pelo jeito 
mais burro, mas mais bunitin ...
"""

import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

'''https://statusinvest.com.br/acoes/embr3'''
 
#Cominho para o chromeDrive funcionar
PATH = 'C:/Users/arthu/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)

#Acessa o site
driver.get('https://statusinvest.com.br/')

#Ativos que irá ser pesquisado no site
ativos = ['EMBR3', 'BBAS3', 'BBSE3', 'ITSA4', 'ABEV3', 'JBSS3', 'PETR3', 'BRDT3', 'VALE3',
          'SANB3', 'ITUB3', 'BIDI3', 'CPFE3', 'FLRY3']


Tabela=[]
for ativo in ativos:   
    
    #Encontra e clica no icone de busca
    icone = driver.find_element_by_class_name('main-search')
    icone.click()
    
    #Enontra a barra de busca e digita o nome da ação
    busca = driver.find_element_by_xpath('//*[@id="main-search"]/div[1]/span[1]/input[2]')
    busca.send_keys(ativo)
    
    #Espera a barra da ação aparecer e clica no ativo.
    ação = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="main-search"]/div[2]/div/div/a/div/div[2]/div/div[2]'))
    )
    ação.click()
    
    #Lê a página e busca alguns indicadore do ativo
    Tabela.append({
        
        'Ativo':((driver.find_element_by_xpath('//*[@id="main-header"]/div/div/div[1]/h1')).text),    
        'Min mês':((driver.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/span[2]')).text),   
        'Max mês':((driver.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/span[2]')).text),   
        'Preço atual':((driver.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong')).text),
        'L/P':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong')).text),
        'V/VP':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[4]/div/div/strong')).text),
        'VPA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong')).text),
        'P/EBIT':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[8]/div/div/strong')).text),
        'P/EBITDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[7]/div/div/strong')).text),
        'EV/EBIT':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[6]/div/div/strong')).text),
        'EV/EBITDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[5]/div/div/strong')).text),
        'D.Y':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong')).text)
        
        })
    
#Cria o DataFrame a partir do dicionário 'Tabela'
df = pd.DataFrame(data=Tabela)

#Salva em em arquivo excel
df.to_excel('D:/Arquivos Perssoais/Finanças/Planilha_automática.xlsx', 'Planilha geral')
driver.quit()

