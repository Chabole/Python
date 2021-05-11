#encoding: utf-8
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 08:51:46 2021

<<< UNESP-FEIS EQUIPE ZEBRA AERODESIGN >>>

__Version__: 0.0.2
__Release__: 06/05/21

@author: Arthur Chabole O. Prudencio
========================
Olá, sou a zebrinha agiota! Mando mensagens mais rápido que vc ... 
    Quem e o que devo cobrar hoje ?

POR FAVOR, USE AS PALAVRAS SEM ACENTO! SOU DISXELICA ... 

"""

from datetime import time
import webbrowser as web
import pyautogui as pg
import time

pg.PAUSE = 0.6

#Função para buscar contato e enviar mensagem 
def busca_contato(contato):   
    width, height = pg.size()
    pg.click(width/4, height*0.23)
    pg.click(width/4, height*0.23)
    pg.press('clear')
    pg.write(contato)
    pg.press('enter')

#Função para enviar mensagem 
def envia_mensagem(mensagem ):
    pg.write(mensagem)
    pg.press('enter')   
    
# Exemplo de variavés quaisquer na mensagem
f= 500      
g= 100   
meses = [1, 2, 8, 4, 7, 10]

#Contatos que deseja enviar a mensagem (sem acento)
contatos = ['Rafael S', 'Gabriel Silva Dos Santos','Jose Victor', 'Lucas Matheus', 
            'Luis Fernando', 'Suino','Vinicius (Zebra)', 'Vitoria']

web.open('https://web.whatsapp.com')
time.sleep(10)

#Iteração para cada contato
for contato, mes in zip(contatos, meses):
    
    #mensagem =  f''''''
    
    # mensagem =  f''' Bom dia {contato}, tudo bem ? Eu sou a zebrinha agiota! Vim lembrar-lo de se cadastrar e criar seu perfil no bitrix24.
    # Coloque suas atividades semanais nos cards e verifique com seu gerente se ja esta incluso em sua area. Caso ja tenha se cadastrado e feito tudo isso desconsidere esta mensagem.
    # Tenha uma bom dia .... att: Zebrinha agiota ;)'''
    
    busca_contato(contato)
    #envia_mensagem(mensagem)








