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
        return f'{self.nome}, S={self.S}, b={self.b}, Clmáx={self.CLmax}'

    
    def V_stall(self, W):
        Vstall = (2*W/(1.225*self.S*self.CLmax))
        return Vstall
    
    def distElip_Sust(self, W):
        y = np.linspace(-self.b/2, self.b/2)
        T0 = (4*(2*W))/(1.225*23*self.b*3.14)
        Le = T0 * ((1-((2*y/self.b)**2))**0.5)
        return y, Le
    
    def efeito_Solo(self, h):
        A = 16*(self.h)/self.b
        return (A**2)/(1 + (A**2))
    
    def Cd_Total(self, Cl):
        Cd = 0.08 + (self.K*(Cl**2)) 
        return Cd
    
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

y1, dist_elip1 = asa_1.distElip_Sust(100)
y2, dist_elip2 = asa_2.distElip_Sust(100)

fig, ax = plt.subplots()
ax.set(title='Distribuição eliptica de sustentação', xlabel='Posição relativa a asa (m)', 
       ylabel='Carregamento (N)')

ax.plot(y1, dist_elip1, label= f'{asa_1}')
ax.plot(y2, dist_elip2, label= f'{asa_2}')

ax.legend()

#==============================================


Cl = np.linspace(0.1, 1.8)

Zb = zp.Airplane(S=0.988, b=2.08, CLmax=1.62)
Zb.C_D0 = 0.08

Cd1 = asa_1.Cd_Total(Cl)
Cd2 = asa_2.Cd_Total(Cl)

fig, ax = plt.subplots()
ax.set(title='Cl x Cd', xlabel='Cd', 
       ylabel='Cl')

ax.plot(Cd1, Cl, label= f'{asa_1}, CD0=0.08')
#ax.plot(Cd2, Cl, label= f'{asa_2}')
ax.plot(Zb.drag_Coef(Cl), Cl, marker='^', label= f'{Zb.name}, S={Zb.S}, b={Zb.b}, CD0={Zb.C_D0}')

ax.set_xlim(0)
ax.legend()