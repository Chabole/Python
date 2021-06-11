# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:54:31 2021

@author: Arthur Chabole
=============================

Primeiros passos com EDO's e solução.

"""

import numpy as np

from scipy.integrate import odeint
from scipy.integrate import quad
from scipy.misc import derivative
import matplotlib.pyplot as plt

from scipy import integrate
import scipy

from ZebraLib.zebralib.zebraperformance import fit
from ZebraLib.zebralib.zebraperformance import Airplane

def EDO_TakeOff(v, t):
    T = Zb.trac_Available(v)
    D = Zb.drag_Force(v, Zb.CLmax)
    R = Zb.mi*(Zb.W - Zb.lift_Force(v, Zb.CLn))
    dvdt = ( T - D - R)/(Zb.M)
    return dvdt

g = 9.81

Zb = Airplane(Load = 5)
Zb2 = Airplane(Load = 11)

#Definindo domínio 
t = np.linspace(1E-3, 6)
y0 = 0

#Descobrindo a função V(t) 
y = odeint(EDO_TakeOff, y0, t)


# ---------------- TESTAR SE VAI FUNCIONAR O MÉTODO ----------------

#Aprox polinômio de 6 grau
pol = fit(t, y, 6)

# Aceleração a(t)
dvdt = derivative(pol, t, dx=1e-6)

# Espaço S(t)
s = quad(pol, 0.5, 4.5)

#Espaço iterado S2(t)
tempo = np.linspace(0.1, 4.5)
#s2 = integrate.cumtrapz(pol(t), tempo) #cumtrapz irá ser derpreciado em 1.6.4

s2 = integrate.cumtrapz(pol(t), t) #cumtrapz irá ser derpreciado em 1.6.4

def func(v):
    T = Zb.trac_Available(v)
    D = Zb.drag_Force(v, Zb.CLn)
    R = Zb.mi*(Zb.W - Zb.lift_Force(v, Zb.CLn))
    
    s =  (v**2)/(T-D-R)*(Zb.M/2)
    
    return s

Zb = Airplane(Load = 5)
Zb2 = Airplane(Load = 8)

g = Zb.takeOff_Distance_EDO()
g2 = Zb2.takeOff_Distance_EDO()

print(f'{g} ------ {g2}')