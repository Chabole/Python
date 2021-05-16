# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:10:56 2021

@author: Arthur Chabole
========================
Testando a classe Asa

"""

from classe_asa import Asa
import numpy as np
import matplotlib.pyplot as plt

#================  PLOTS Cd e dist de sustentação  =================

asa_1  = Asa('Asa 1', 0.988, 2.08, 1.62)
asa_2  = Asa('Asa 2', 0.868, 2.5, 1.5)
asa_3  = Asa('Asa 3', 1.1, 2.7, 1.5)

Asas = np.array((asa_1, asa_2, asa_3))

fig, ax = plt.subplots()
ax.set(title='Cl x Cd', 
        xlabel='Cd', 
        ylabel='Cl')

fig, ax2 = plt.subplots()
ax2.set(title='Distribuição eliptica de sustentação', 
        xlabel='Posição relativa a asa (m)', 
        ylabel='Carregamento (N)')

for asa in Asas:
    Cd = asa.Cd_Total()
    ax.plot(Cd, asa.Cl, label= f'{asa}')
    
    y, dist_elip = asa.distElip_Sust(140)
    ax2.plot(y, dist_elip, label= f'{asa}')

ax.set_xlim(0)
ax.legend()
ax.grid(linestyle='--')

ax2.legend()
ax2.grid(linestyle='--')

