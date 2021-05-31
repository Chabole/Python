# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:24:00 2021

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

dados_df = pd.read_excel('D:/Arquivos Perssoais/PythonProjects/Projetos de automação/Ações_listadas_B3.xlsx')

# tabela = []   
# for ativo in dados_df['Código']:
    
#     html = urlopen(f"https://statusinvest.com.br/acoes/{ativo}").read()
#     soup = BeautifulSoup(html, 'html.parser')
    
#     tabela.append({
        
#         'Nome':(soup.find(class_="value d-block lh-4 fs-4 fw-700")).text, 
#         #'Código':(soup.find_all(class_='table-date-value')).text

#         })
    
    
