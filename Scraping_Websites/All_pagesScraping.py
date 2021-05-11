# -*- coding: utf-8 -*-
"""
Created on Thu May  1 13:18:33 2021

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
soup = BeautifulSoup(html, 'html.parser')

#Encontarndos todos os links das páginas
links = soup.find(class_="ui-search-pagination andes-pagination")

#Extraindo só o texto
all_links = []
for link in links:
    all_links.append(link.find(class_='andes-pagination__link ui-search-link')['href'])
    
'''

Iteração para todos os links. Criar um objeto a partir do link, extrair o texto dos atributos desejados
    armazenar em um dicionário. Seguir para proxima página e repetir o processo.

'''

def scraping_data(all_links):
    '''
    Parameters
    ----------
    all_links : array
        Array de links que se deseja extrair dados.

    Returns
    -------
    tabela_df : DataFrame
        Dicionário com o modelo, preço, local e ano dos carros.

    '''
    tabela = []
    for link in all_links:
        response = (urlopen(link))
        html = response.read()
        
        soup = BeautifulSoup(html, 'html.parser') #Inst objeto 
        blocos = soup.find_all(class_='ui-search-layout ui-search-layout--grid') #Pegando classes específicas
        
        for bloco in blocos:
            tabela.append({
                
                'Modelo':(bloco.find(class_="ui-search-item__title ui-search-item__group__element")).text,
                'Preços':float((bloco.find(class_="price-tag-fraction")).text),
                'Local':(bloco.find(class_="ui-search-item__group__element ui-search-item__location")).text,
                'Ano':float((bloco.find_all(class_="ui-search-card-attributes__attribute")[0]).text),
                'Km':((bloco.find_all(class_="ui-search-card-attributes__attribute")[1]).text) #Remover o 'Km'
                })
            
    #Criando um dataframe e alimentando com um dicionário
    tabela_df = pd.DataFrame(data=tabela)
    
    return tabela_df
            
pag_df = scraping_data(all_links)

#Salvando o DataFrame em um arquivo excel
pag_df.to_excel("D:/Arquivos Perssoais/PythonProjects/Projetos de automação/Mercado_livre.xlsx",
                sheet_name='Tabela') 


sns.pairplot(pag_df, diag_kind='kde')
sns.barplot(x='Local', y='Preços', data=pag_df)

print(pag_df.tail())


