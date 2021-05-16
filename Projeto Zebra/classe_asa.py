# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================

"""

import numpy as np
import matplotlib.pyplot as plt
import ZebraLib.zebralib.zebraperformance as zp 

class Asa:
    def __init__(self, nome, S, b, CLmax):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        
        self.AR = (self.b**2)/self.S
        self.K = 1/(3.14*0.75*self.AR)
        
        #self.cl = np.linspace(0.1, self.CLmax)
    
    def __repr__(self):
        self.AR = round(self.AR,2)
        return f'{self.nome}, S={self.S},\
    b={self.b}, AR={self.AR}'
                    
    def V_stall(self, W):
        Vstall = (2*W/(1.225*self.S*self.CLmax))
        return Vstall
    
    def distElip_Sust(self, W):
        y = np.linspace(-self.b/2, self.b/2, 500)
        A = 4*(2.3*W)/(self.b*3.14)
        Le = A*((1-((2*y/self.b)**2))**0.5)
        return y, Le
    
    def momento_Fletor(self, W):
        y, Le = self.distElip_Sust(W)
        M = abs(y*Le)
        return M
    
    def Cd_Total(self, Cl):
        Cd = 0.08 + (self.K*(Cl**2)) 
        return Cd
    
# #===================================================    
    
    
# asa_1  = Asa('Asa 1', 0.988, 2.08, 1.62)
# asa_2  = Asa('Asa 2', 0.868, 2.5, 1.5)
# asa_3  = Asa('Asa 3', 1.3, 2.5, 1.5)

# Asas = np.array((asa_1, asa_2, asa_3))
# Cl = np.linspace(0.1, 1.8)

# #================  PLOTS COM OBJETOS  =================

# fig, ax = plt.subplots()
# ax.set(title='Cl x Cd', 
#         xlabel='Posição relativa a asa (m)', 
#         ylabel='Carregamento (N)')

# fig, ax2 = plt.subplots()
# ax2.set(title='Distribuição eliptica de sustentação', 
#        xlabel='Cd', 
#        ylabel='Cl')

# for Asa in Asas:
#     Cd = Asa.Cd_Total(Cl)
#     ax.plot(Cd, Cl, label= f'{Asa}')
    
#     y, dist_elip = Asa.distElip_Sust(140)
#     ax2.plot(y, dist_elip, label= f'{Asa}')

# ax.set_xlim(0)
# ax.legend()
# ax.grid(linestyle='--')

# ax2.legend()
# ax2.grid(linestyle='--')

