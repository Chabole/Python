# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:18:01 2021

@author: Arthur Chabole
=============================
Visualização de indicadores fundamentalistas.

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def full_word(x):
    if x == '-' or x == '-%' or x==' -':    
        x = str(x.replace("-","NaN"))
    return x

tabela_df = pd.read_excel('D:/Arquivos Perssoais/Finanças/Planilha_automática.xlsx') 

#Tratando os valores para floats
for coluna in range(len(tabela_df.columns)-1):
    index = tabela_df.columns[coluna+1]
    
    tabela_df[index] = tabela_df[index].apply(lambda x: (x.replace("R$","")))
    tabela_df[index] = tabela_df[index].apply(lambda x: (full_word(x)))
    tabela_df[index] = tabela_df[index].apply(lambda x: (x.replace("%","")))
    try:
        tabela_df[index] = tabela_df[index].apply(lambda x: float(x.replace(".","").replace(",",".")))    
    except:
        print('Something wrong!')

#Tratando os NaN
tabela_df = tabela_df.fillna(0)

#Salvando 
tabela_df.to_excel('D:/Arquivos Perssoais/Finanças/Planilha_automática_formatada.xlsx') #tirar o index

# #plots
# for coluna in range(len(tabela_df.columns)-1):
#     index = tabela_df.columns[coluna+1]
    
#     fig, ax = plt.subplots()
#     sns.barplot(x='Ativo', y=tabela_df[index], data=tabela_df)
#     plt.ylim(-10, 50)
#     print(coluna)






