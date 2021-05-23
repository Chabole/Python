# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================
Classe wing

"""
import numpy as np
import matplotlib.pyplot as plt
from ZebraLib.zebralib.zebra_wing import integral
from ZebraLib.zebralib.zebraperformance import Airplane

class Asa:
    def __init__(self, nome, S, b, CLmax, W=140):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        self.W = W
        
        self.AR = (self.b**2)/self.S
        self.K = 1/(3.14*0.75*self.AR)
        self.Cl = np.linspace(0.1, self.CLmax)
    
    def __str__(self):
        self.AR = round(self.AR,2)
        return f'{self.nome}, S={self.S},\
    b={self.b}, AR={self.AR}'
                    
    def V_stall(self, W):
        Vstall = (2*W/(1.225*self.S*self.CLmax))
        return Vstall
    
    def Cd_Total(self):
        Cd = 0.08 + (self.K*(self.Cl**2)) 
        return Cd
    
    def distElip_Sust(self, W):
        y = np.linspace(-self.b/2, self.b/2, 500)
        A = 4*(2.3*W)/(self.b*3.14)
        Le = A*((1-((2*self.y/self.b)**2))**0.5)
        return Le
    
    def força_Cortante(self, W):
        V=[]
        d=0.03
        L = self.distElip_Sust(W)
        y = self.y
        F = integral(L, y, y.min(), y.max())
        for i in range(0,len(y)):
            if y[i] < (-d/2):
                V.append(integral(L,y,y.min(),y[i]))
            if y[i]>(-d/2) and y[i]<(d/2):
                V.append(integral(L,y,y.min(),y[i])-F/2)
            if y[i]>(d/2):
                V.append(integral(L, y, y.min(), y[i])-F)   
        return V
    
    def moment_Fletor(self, W):
        V = self.força_Cortante(W)
        y = self.y
        M=[]
        for i in range(0, len(y)):
            M.append(integral(V, y, y.min(), y[i]))
        for i in range(0,len(y)):
            M[-i]=M[i]
        return M
    
    def import_dados(self, Local_nome, Planilha):
        a, cl, cd = Airplane.import_WingData(Local_nome, Planilha)
        return a, cl, cd
        
avião = Airplane()
Cl3 = np.linspace(0.1, 1.9)
cd3 = avião.drag_Coef(Cl3)
    
Zb1 = Asa('Asa 1', 0.988, 2.08, 1.7)
Zb2 = Asa('Asa 2', 1, 3, 2.08, 1.9)

a1, cl1, cd1 = Zb1.import_dados('D:/UNESP/AeroDesign/Códigos_Python/Dados/dados_asas.xlsx', 'Planilha1')
a2, cl2, cd2 = Zb2.import_dados('D:/UNESP/AeroDesign/Códigos_Python/Dados/dados_asas.xlsx', 'Planilha2')

fig, ax = plt.subplots()
ax.plot(cd1, cl1, label='Zb1')
ax.plot(cd2, cl2, label='Zb2')
ax.plot(cd3, Cl3, label='Avião sem efeito solo')
ax.plot(avião.drag_Coef(Ground_Effect=True, CL=Cl3), Cl3, '--', label='Avião com efeito solo')
ax.legend()

# Zb1 = Asa('Asa 1', 0.988, 2.08, 1.7)
# Zb2 = Asa('Asa 2', 1, 3, 2.08, 100)
# Zb3 = Asa('Asa 2', 1, 3, 2.08, 100)
# Zb4 = Asa('Asa 2', 1, 3, 2.08, 100)

# Aviões = np.array((Zb1, Zb2, Zb3, Zb4))
# W = np.linspace(85, 140, 4)


# fig, ax = plt.subplots()
# ax.set(title=f'Força cortante para pesos de {W.min()}N até {W.max()}N',
#         xlabel='envergadura [m]', ylabel='Momento fletor [N]')

# fig, ax2 = plt.subplots()
# ax2.set(title=f'Momento fletor para pesos de {W.min()}N até {W.max()}N',
#         xlabel='envergadura [m]', ylabel='Momento fletor [N]')

# fig, ax3 = plt.subplots()
# ax3.set(title=f'Distribuição de sustentação para pesos de {W.min()}N até {W.max()}N',
#         xlabel='envergadura [m]', ylabel='Momento fletor [N]')

# for Zb, w in zip (Aviões, W):
#     w = round(w)
#     V = Zb.força_Cortante(w)
#     ax.plot(Zb.y, V, label=f'W={w}N')
    
#     M = Zb.moment_Fletor(w)
#     ax2.plot(Zb.y, M, label=f'W={w}N')
    
#     L = Zb.distElip_Sust(w)
#     ax3.plot(Zb.y, L, label=f'W={w}N')
    
    
    
# ax.legend()
# ax2.legend()
# ax3.legend()






