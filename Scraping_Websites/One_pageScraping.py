# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:39:50 2021

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
html = urlopen('https://lista.mercadolivre.com.br/carros#D[A:carros]').read()
soup = BeautifulSoup(html, 'html.parser') #Inst objeto 

#Bloco das informações
blocos = soup.find_all(class_='ui-search-layout ui-search-layout--grid') #Pegando classes específicas

#Iterando para todos os blocos
tabela = []
for bloco in blocos:
    tabela.append({
        
        'Modelo':(bloco.find(class_="ui-search-item__title ui-search-item__group__element")).text,
        'Preços':float((bloco.find(class_="price-tag-fraction")).text),
        'Local':(bloco.find(class_="ui-search-item__group__element ui-search-item__location")).text,
        'Ano':float((bloco.find_all(class_="ui-search-card-attributes__attribute")[0]).text),
        'Km':((bloco.find_all(class_="ui-search-card-attributes__attribute")[1]).text) #Problema com isso
        })
    

#Criando um dataframe e alimentando com um dicionário
pag_df = pd.DataFrame(data=tabela)


#Salvando o DataFrame em um arquivo excel
pag_df.to_excel("D:/Arquivos Perssoais/PythonProjects/Projetos de automação/Mercado_livre.xlsx",
                sheet_name='Tabela') 

print(pag_df.tail())