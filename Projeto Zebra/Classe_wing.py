# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================

"""

import numpy as np
import matplotlib.pyplot as plt
import ZebraLib.zebralib.zebraperformance as zp 

class Wing:
    
    def __init__(self, nome, S, b, CLmax):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        
        self.AR = (self.b**2)/self.S
        self.K = 1/(3.14*0.75*self.AR)
    
    def __repr__(self):
        self.AR = round(self.AR,2)
        return f'{self.nome}, S={self.S}, \
    b={self.b}, AR={self.AR}'
                    
    def V_stall(self, W):
        Vstall = (2*W/(1.225*self.S*self.CLmax))
        return Vstall
    
    def distElip_Sust(self, W):
        y = np.linspace(-self.b/2, self.b/2)
        
        A = 4*(2.3*W)/(self.b*3.14)
        Le = A*((1-((2*y/self.b)**2))**0.5)
        return y, Le
    
    def Cd_Total(self, Cl):
        Cd = 0.08 + (self.K*(Cl**2)) 
        return Cd
    
#===================================================    
    
    
asa_1  = Wing('Asa 1', 0.988, 2.08, 1.62)
asa_2  = Wing('Asa 2', 0.868, 2.5, 1.5)
asa_3  = Wing('Asa 3', 1.3, 2.5, 1.5)

Asas = np.array((asa_1, asa_2, asa_3))

# y1, dist_elip1 = asa_1.distElip_Sust(140)
# y2, dist_elip2 = asa_2.distElip_Sust(140)
# y3, dist_elip3 = asa_3.distElip_Sust(140)

# fig, ax = plt.subplots()
# ax.set(title='Distribuição eliptica de sustentação', 
#        xlabel='Posição relativa a asa (m)', 
#        ylabel='Carregamento (N)')

# ax.plot(y1, dist_elip1, label= f'{asa_1}')
# ax.plot(y2, dist_elip2, label= f'{asa_2}')
# ax.plot(y3, dist_elip3, label= f'{asa_3}')

# ax.legend()
# ax.grid(linestyle='--')

# #==============================================

Cl = np.linspace(0.1, 1.8)

# Cd1 = asa_1.Cd_Total(Cl)
# Cd2 = asa_2.Cd_Total(Cl)
# Cd3 = asa_3.Cd_Total(Cl)

# fig, ax = plt.subplots()
# ax.set(title='Cl x Cd', xlabel='Cd', 
#         ylabel='Cl')

# ax.plot(Cd1, Cl, label= f'{asa_1}, AR={asa_1.AR}')
# ax.plot(Cd2, Cl, label= f'{asa_2}, AR={asa_2.AR}')
# ax.plot(Cd3, Cl, label= f'{asa_3}, AR={asa_3.AR}')

# ax.set_xlim(0)
# ax.legend()
# ax.grid(linestyle='--')

#================  PLOTS COM OBJETOS  =================

fig, ax = plt.subplots()
ax.set(title='Distribuição eliptica de sustentação', 
       xlabel='Cd', 
       ylabel='Cl')

fig, ax2 = plt.subplots()
ax2.set(title='Cl x Cd', 
        xlabel='Posição relativa a asa (m)', 
        ylabel='Carregamento (N)')

for Asa in Asas:
    Cd = Asa.Cd_Total(Cl)
    ax.plot(Cd, Cl, label= f'{Asa}')
    
    y, dist_elip = Asa.distElip_Sust(140)
    ax2.plot(y, dist_elip, label= f'{Asa}')

ax.set_xlim(0)
ax.legend()
ax.grid(linestyle='--')

ax2.legend()
ax2.grid(linestyle='--')

