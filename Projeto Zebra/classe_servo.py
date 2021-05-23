# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

   
class Servo:
    
    def __init__(self, nome):
        self.nome = nome

    def importar_Dados(self, Local_nome):
        df = pd.read_excel(Local_nome)
        return df

servo_1 = Servo('Servo 1')
tabela = servo_1.importar_Dados('D:/UNESP/AeroDesign/Códigos_Python/Dados/Servo_Data.xlsx')
        
eq_reta = np.polyfit(tabela['Torque'], tabela['Corrente'], 2)

fig, ax_1 = plt.subplots()
ax_1.set(title='Corrente x Torque')

r = sns.regplot(x='Torque', y='Corrente', data=tabela, ax=ax_1, ci=False)     