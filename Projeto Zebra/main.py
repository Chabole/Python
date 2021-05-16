# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:10:56 2021

@author: Arthur Chabole
========================

"""
from classe_asa import Asa
import numpy as np
import matplotlib.pyplot as plt

asa_1 = Asa('Asa 1', 0.988, 2.08, 1.62)

Le = asa_1.distElip_Sust(140)
M = asa_1.momento_Fletor(140)

fig, ax_1 = plt.subplots()
ax_1.set(title=f'{asa_1}', xlabel='Envergadura(m)',
       ylabel='Valor numérico')

ax_1.plot(Le[0], M , label='Momento fletor')
ax_1.plot(Le[0], Le[1], label='Distribuição elíptica de sustentação')

ax_1.legend()
