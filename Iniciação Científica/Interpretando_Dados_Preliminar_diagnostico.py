# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:56:34 2020

@author: Arthur Chabole

// Visualização dos dados do motor em estado de falha e normal
Este programa importa dados em .txt e gera um 2 subgráfico apartir dos valores
                                    do arquivo txt

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
                                              #Carregando os dados do bloco de notas 
df_falha =  pd.read_csv('D:/UNESP/Iniciação/Dados/Dados/Todos_FAL.txt', delimiter = "\t")                       
df_normal =  pd .read_csv('D:/UNESP/Iniciação/Dados/Dados/Todos_NOR.txt', delimiter = "\t")  

    #Definir domínio do plot
Dom= 5000

                     #Separando as colunas dos aquivos .txt_eixo_certo
#Vet_x1 = df_normal['x']
Vet_yx = df_normal['AcX']
Vet_yy = df_normal['AcY']
Vet_yz = df_normal['AcZ']
Vet_x1 = np.linspace(0,len(Vet_yx),len(Vet_yx))

#Vet_x2 = df_falha['x']
Vet_yx2 = df_falha['AcX']
Vet_yy2 = df_falha['AcY']
Vet_yz2 = df_falha['AcZ']
Vet_x2 = np.linspace(0,len(Vet_yx2),len(Vet_yx2))
              
                        #Criando objeto p/ gráfico 1 e 2
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle(' Sinal Normal e em falha ')
                                    #Configurando layout do gráfico falha cima/normal baixo                             
ax1.plot(Vet_x1, Vet_yx, label= 'Eixo X', color= 'r')
ax1.plot(Vet_x1, Vet_yy, label= 'Eixo Y', color= 'blue')
ax1.plot(Vet_x1, Vet_yz, label= 'Eixo Z', color= 'lime')
ax1.set_ylabel('Sinal Normal')
ax1.axis(xmin=0, xmax = Dom)
ax1.legend()

ax2.plot(Vet_x2, Vet_yx2, label= 'Eixo X', color= 'r')
ax2.plot(Vet_x2, Vet_yy2, label= 'Eixo Y', color= 'blue')
ax2.plot(Vet_x2, Vet_yz2, label= 'Eixo Z', color= 'lime')
ax2.set_ylabel('Sinal em Falha')
ax2.axis(xmin=0, xmax = Dom)
ax2.legend()
























