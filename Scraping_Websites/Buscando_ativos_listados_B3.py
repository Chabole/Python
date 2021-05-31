# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:39:34 2021

@author: Arthur Chabole
=============================
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from urllib.request import urlopen

#Entrando no site e roubando o source_code
html = urlopen('https://valorinveste.globo.com/cotacoes/').read()
soup = BeautifulSoup(html, 'html.parser')

'''

Iteração para todos os links. Criar um objeto a partir do link, extrair o texto dos atributos desejados
    armazenar em um dicionário. Seguir para proxima página e repetir o processo.

'''
   
blocos = soup.find_all(class_='table-date-value') #Pegando classes específicas
   
#blocos = (soup.find_all(class_='table-date-value')[6]).text #Pegando 

tabela = []   
nome, codigo = 5, 6
for index in range(168):
    tabela.append({
        
        'Nome':(soup.find_all(class_='table-date-value')[nome]).text, 
        'Código':(soup.find_all(class_='table-date-value')[codigo]).text

        })
    
    nome += 5
    codigo += 5
    
#Criando um dataframe e alimentando com um dicionário
tabela_df = pd.DataFrame(data=tabela)
    
#Salvando o DataFrame em um arquivo excel
tabela_df.to_excel("D:/Arquivos Perssoais/PythonProjects/Projetos de automação/Ações_listadas_B3.xlsx",
                sheet_name='Planilha1') 






