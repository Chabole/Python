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
        
        self.AR = (self.b**2)/self.S
        self.y = np.linspace(-self.b/2, self.b/2)
        
    def V_stall(self, rho):
        return (2*self.W/(rho*self.S*self.CLmax))**0.5
    
    def distElip_Sust(self, W=140):
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

    
    
    
    