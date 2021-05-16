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
        Le = A*((1-((2*y/self.b)**2))**0.5)
        return y, Le
    
    def Nmax(self, W, v):
        data = zp.import_WingData()
        
        
    

