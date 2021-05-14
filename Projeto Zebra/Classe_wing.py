# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================

"""

import numpy as np
import matplotlib.pyplot as plt

class Wing:
    
    def __init__(self, nome, S, b, CLmax):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        
        self.AR = (self.b**2)/self.S
    
    def V_stall(self, W):
        Vstall = (2*W/(1.225*self.S*self.CLmax))
        return Vstall
    
    def distElip_Sust(self, W):
        y = np.linspace(-self.b/2, self.b/2)
        
        T0 = (4*(2*W))/(1.225*23*self.b*3.14)
        Le = T0 * ((1-((2*y/self.b)**2))**0.5)
        return y, Le
    
    #Problema
    def distRetang_Sust(self, W):
        
        y = np.linspace(-self.b/2, self.b/2)
        
        lamb = 0.841/3.36
        A = (2*(2*W))/((1 + lamb)*self.b)
        B = (2*y*(lamb - 1))/self.b
    
        Lt = A*((1 + (B))**0.5)
        
        return Lt
    

asa_1  = Wing('Asa 1', 0.988, 2.08, 1.62)
asa_2  = Wing('Asa 2', 0.868, 2.2, 1.5)

# y = np.linspace(-asa_1.b/2, asa_1.b/2)
# y = np.linspace(-asa_1.b/2, asa_1.b/2)

y1, dist_elip1 = asa_1.distElip_Sust(100)
y2, dist_elip2 = asa_2.distElip_Sust(100)

fig, ax = plt.subplots()
ax.set(title='Distribuição de sustentação', xlabel='Posição relativa a asa (m)', 
       ylabel='Carregamento (N)')

ax.plot(y1, dist_elip1, label= f'Dist Eliptica {asa_1.nome}')
ax.plot(y2, dist_elip2, label= f'Dist Eliptica {asa_2.nome}')

ax.legend()
