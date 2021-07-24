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

def full_word(x):
    if x == '-' or x == '-%' or x==' -':    
        x = str(x.replace("-","NaN"))
    return x

'''https://statusinvest.com.br/acoes/embr3'''
 
#Cominho para o chromeDrive funcionar
PATH = 'C:/Users/arthu/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)

#Acessa o site
driver.get('https://statusinvest.com.br/')

# #Ativos que irá ser pesquisado no site
# ativos = ['EMBR3', 'BBAS3', 'BBSE3', 'ITSA4', 'ABEV3', 'JBSS3', 'PETR3', 'BRDT3', 'VALE3',
#           'SANB3', 'ITUB3', 'BIDI3', 'CPFE3', 'FLRY3']

#ativos = ['EMBR3', 'BBAS3', 'BBSE3']

dados_df = pd.read_excel('D:/Arquivos Perssoais/Finanças/Planilha_automática_New.xlsx', sheet_name='Sheet2')


del_list = ['BAHI11', 'BTTL3', 'EQMA3B', 'CEED4']

for delete in del_list:
    
    # Get names of indexes for which column Stock has value No
    indexNames = dados_df[dados_df['Papel'] == delete].index
    
    # Delete these row indexes from dataFrame
    dados_df.drop(indexNames , inplace=True)

ativos = dados_df['Papel']



Tabela=[]
for i, ativo in enumerate(ativos):   
    print(f'{ativo} iteração {i}')
    #@ID_XPATH variáveis
    icone_class = 'main-search'
    busca_xpath = '//*[@id="main-search"]/div[1]/span[1]/input[2]'
    ação_xpath = '//*[@id="main-search"]/div[2]/div/div/a/div/div[2]/div/div[2]'
    
    #Encontra e clica no icone de busca    
    icone = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.CLASS_NAME, icone_class)))
    icone.click()
    
    #Enontra a barra de busca e digita o nome da ação    
    busca = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.XPATH, busca_xpath)))
    busca.send_keys(ativo)

    try:
        
        #Espera a barra da ação aparecer e clica no ativo.
        ação = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.XPATH, ação_xpath)))
    
        ação.click()
        
        #Lê a página e busca alguns indicadore do ativo
        Tabela.append({
            
            #Ativo
            'Código': ativo,
            'Ativo':((driver.find_element_by_xpath('//*[@id="main-header"]/div/div/div[1]/h1')).text),   
            'Setor':(driver.find_element_by_xpath('//*[@id="company-section"]/div/div[3]/div/div[1]/div/div/div/a/strong')).text,
            'Sub setor':(driver.find_element_by_xpath('//*[@id="company-section"]/div/div[3]/div/div[2]/div/div/div/a/strong')).text,
            
            #Preço
            'Min mês':((driver.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/span[2]')).text),   
            'Max mês':((driver.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/span[2]')).text),   
            'Preço atual':((driver.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong')).text),
            
            #Indicadores de valuation
            'L/P':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong')).text),
            'V/VP':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[4]/div/div/strong')).text),
            'VPA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong')).text),
            'LPA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[11]/div/div/strong')).text),
            'PEG RATIO':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[3]/div/div/strong')).text),
            'P/EBIT':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[8]/div/div/strong')).text),
            'P/EBITDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[7]/div/div/strong')).text),
            'EV/EBIT':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[6]/div/div/strong')).text),
            'EV/EBITDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[5]/div/div/strong')).text),
            'D.Y':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong')).text),
            
            #Indicadores de endividamento
            'Passivo/Ativos':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[5]/div/div/strong')).text),
            'Divida/PL':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[1]/div/div/strong')).text),
            'LIQ.CORRENTE':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[6]/div/div/strong')).text),
            'DÍV.LÍQUIDA/EBIT':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[3]/div/div/strong')).text),
            'DÍV.LÍQUIDA/EBITDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[2]/div/div/strong')).text),
    
            #Indicadores de eficiência
            'M. LÍQUIDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div/div/strong')).text),
            'M. EBITDA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[2]/div/div/strong')).text),
    
            #Indicadores de rentabilidade 
            'ROE':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[1]/div/div/strong')).text),
            'ROIC':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[3]/div/div/strong')).text),
            'ROA':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[2]/div/div/strong')).text),
            'GIRO ATIVOS':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[4]/div/div/strong')).text),
            
            #Incadores de crescimento
            'CAGR Receitas 5 anos':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[1]/div/div/strong')).text),
            'CAGR Lucros 5 anos':((driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[2]/div/div/strong')).text)
            })
    except:
        continue

driver.quit()

#Cria o DataFrame a partir do dicionário 'Tabela'
tabela_df = pd.DataFrame(data=Tabela)

#Tratando os valores para floats
for coluna in range(len(tabela_df.columns)-4):
    index = tabela_df.columns[coluna+4]
    
    tabela_df[index] = tabela_df[index].apply(lambda x: (x.replace("R$","")))
    tabela_df[index] = tabela_df[index].apply(lambda x: (full_word(x)))
    tabela_df[index] = tabela_df[index].apply(lambda x: (x.replace("%","")))
    try:
        tabela_df[index] = tabela_df[index].apply(lambda x: float(x.replace(".","").replace(",",".")))    
    except:
        print(f'Vish! algum deu errado com a coluna {index}')

#Tratando os NaN
tabela_df = tabela_df.fillna(0)

#Salvando em arquivo excel
tabela_df.to_excel('D:/Arquivos Perssoais/Finanças/B3_ATIVOS.xlsx') #tirar o index
