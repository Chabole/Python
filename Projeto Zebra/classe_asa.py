# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:44 2021

@author: Arthur Chabole
========================
Classe wing

"""

import numpy as np
import matplotlib.pyplot as plt

class Wing:
    
    def __init__(self, nome, S, b, CLmax, W=None):
        self.nome = nome
        self.S = S
        self.b = b
        self.CLmax = CLmax
        self.W = W
        
        self.AR = (self.b**2)/self.S
    
    def V_stall(self, rho):
        self.rho = rho
        return (2*self.W/(rho*self.S*self.CLmax))**0.5

        
Zb_1 = Wing('Asa 1', 0.988, 2.08, 1.7)
Zb_2 = Wing('Asa 2', 1, 2.2, 1.5)
Zb_3 = Wing('Asa 3', 2, 3, 1.95)

asas = np.array((Zb_1, Zb_2, Zb_3))
We = np.array((140, 150, 160))

Zb_1.V_stall()







