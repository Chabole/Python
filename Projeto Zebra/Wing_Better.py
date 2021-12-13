# -*- coding: utf-8 -*-
"""
Created on Wed May 19 12:29:09 2021

@author: Arthur Chabole
=============================
"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.integrate import quad   
from ZebraLib.zebralib.zebra_wing import integral

class Wing:
    def __init__(self, nome, S, b, CLmax, W=140):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        self.W = W
        
        self.AR = (self.b**2)/self.S
        self.y = np.linspace(-self.b/2, self.b/2, 100)
        
    def V_stall(self, rho):
        self.rho = rho
        return (2*self.W/(rho*self.S*self.CLmax))**0.5
    
    def distElip_Sust(self, W):
        A = 4*(2.3*W)/(self.b*3.14)
        Le = A*((1-((2*self.y/self.b)**2))**0.5)
        return Le
    
    def força_Cortante(self, W):
        V=[]
        d=0.03
        L = self.distElip_Sust(W)
        F = integral(L,self.y,self.y.min(),self.y.max())
        #F = quad(L,self.y.min(),self.y.max())
        
        for i in range(0,len(self.y)):
            if self.y[i] < (-d/2):
                V.append(integral(L,self.y,self.y.min(),self.y[i]))
                #V.append(quad(L,self.y.min(),self.y[i])-F/2)
            if self.y[i]>(-d/2) and self.y[i]<(d/2):
                V.append(integral(L,self.y,self.y.min(),self.y[i])-F/2)
                #V.append(quad(L,self.y.min(),self.y[i])-F/2)
            if self.y[i]>(d/2):
                V.append(integral(L,self.y,self.y.min(),self.y[i])-F)
                #V.append(quad(L,self.y.min(),self.y[i])-F)
        return V
        
    def moment_Fletor(self, V):
        M=[]
        for i in range(0,len(self.y)):
            M.append(integral(V,self.y,self.y.min(),self.y[i]))
        for i in range(0,len(self.y)):
            M[-i]=M[i]
        return M
    
Zb = Wing('Asa 1', 0.988, 2.08, 1.7, 140)
Zb2 = Wing('Asa 1', 0.888, 2.4, 1.7, 120)
Zb3 = Wing('Asa 1', 0.788, 2.64, 1.7, 143)
Zb4 = Wing('Asa 1', 1, 1.9, 1.7, 160)

Peso = np.linspace(85,150,5)

fig, ax = plt.subplots()
fig, ax2 = plt.subplots()

ax.set(title=f'Momento fletor para pesos de {Peso.min()}N até {Peso.max()}N', 
       xlabel='envergadura [m]', ylabel='Força cortante [N]')

ax2.set(title=f'Força cortante para pesos de {Peso.min()}N até {Peso.max()}N',
        xlabel='envergadura [m]', ylabel='Momento fletor [N]')

#Cores = np.array(('#64F9F2', '#66FF7C','#EBA2F5','#FCF58D', '#25FFF6'))

for w in (Peso):
    V = Zb.força_Cortante(w)
    M = Zb.moment_Fletor(V)
    ax.plot(Zb.y, V, label=f'W={w}N')
    ax2.plot(Zb.y, M, label=f'W={w}N')

ax.set_facecolor('oldlace')
ax2.set_facecolor('oldlace')
ax.legend()
ax2.legend()
ax.grid(linestyle='dotted')
ax2.grid(linestyle='dotted')

