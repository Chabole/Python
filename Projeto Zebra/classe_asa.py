  # -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================
Classe wing

"""

import numpy as np
#import matplotlib.pyplot as plt
#import ZebraLib.zebralib.zebraperformance as zp 
#from ZebraLib.zebralib.zebraperformance import Airplane

class Asa:
    
    def __init__(self, nome, S, b, CLmax):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        
        self.AR = (self.b**2)/self.S
        self.K = 1/(3.14*0.75*self.AR)
        
        self.Cl = np.linspace(0.1, self.CLmax)
    
    def __str__(self):
        self.AR = round(self.AR,2)
        return (f'{self.nome}, S={self.S},\
    b={self.b}, AR={self.AR}')
                    
    def V_stall(self, W):
        
        Vstall = (2*W/(1.225*self.S*self.CLmax))**0.5
        return Vstall
    
    def distElip_Sust(self, W):
        y = np.linspace(-self.b/2, self.b/2, 500)
        A = 4*(2.3*W)/(self.b*3.14)
        Le = A*((1-((2*y/self.b)**2))**0.5)
        return y, Le

    def Cd_Total(self):
        Cd = 0.08 + (self.K*(self.Cl**2)) 
        return Cd
    
    def momento_Fletor(self, W):
        y, Le = self.distElip_Sust(W)
        M = abs(y*Le)
        return M

class Aileron:
    def __init__(self, nome, S, b):
        self.nome = nome
        self.S = S
        self.b = b
    
    def volume_h(self):
        pass
        
# # #===================================================    

# asa_1 = Asa('Asa 1', 0.988, 2.08, 1.62)
# asa_2 = Asa('Asa 2', 0.868, 2.5, 1.5)
# asa_3 = Asa('Asa 3', 1.2, 2.65, 1.5)

# Asas = np.array((asa_1, asa_2, asa_3))

# #================  PLOTS COM OBJETOS  =================

# fig, ax = plt.subplots()
# ax.set(title='Distribuição eliptica de sustentação', 
#         xlabel='Posição relativa a asa (m)',
#         ylabel='Carregamento (N)')

# fig, ax2 = plt.subplots()
# ax2.set(title='Cl x Cd', 
#         xlabel='Cd',
#         ylabel='Cl')

# for Asa in Asas:
    
#     y, dist_elip = Asa.distElip_Sust(140)
#     ax.plot(y, dist_elip, label= f'{Asa}')
    
#     Cd = Asa.Cd_Total()
#     ax2.plot(Cd, Asa.Cl, label= f'{Asa}')

# ax.legend()
# ax.grid(linestyle='--')

# ax2.set_xlim(0)
# ax2.legend()
# ax2.grid(linestyle='--')
        """

        Calcula a velocidade de estoll da asa        

        Parameters
        ----------
        W : floar ou array
            Valor(s) do peso da aeronave.

        Returns
        -------
        Vstall : float ou array
            Velocidade de estoll.
            
        Examples
        -------
        >>> import numpy
        
        >>> asa_1 = Wing('Asa 1', 0.988, 2.08, 1.62)

        """