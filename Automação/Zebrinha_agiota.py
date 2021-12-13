# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:01:26 2021

__Version__: 0.0.3

__Release__: 17/05/2021

@author: Arthur Chabole
====================================================================
EQUIPE ZEBRA AERODESIGN 2021 - ZEBRINHA AGIOTA
=====================================================================
Passos para usar a zebrinha agiota
0. Esteja com o  pacote anaconda instalado https://www.anaconda.com/products/individual
1. Instale o chrome driver https://sites.google.com/a/chromium.org/chromedriver/downloads
2. Instale ou verifique se as bibliotecas selenium e BeautilfulSoup
    2.1 Caso não esteja instalado vá no console do python e digite
    2.2 pip install selenium (precione enter e espere instalar)
    2.3 pip install BeautilfulSoup (precione enter e espere instalar)

"""

import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui 
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup 

class Zebrinha:
    
    #Colocar os XPATH aqui (selenium)
    Barra_pesquisa = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    Barra_mensagem = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    Barra_grupo = '//*[@id="main"]/header/div[2]/div[1]/div/span'
    Barra_docs = "kia3R _2wzbH"
    Botão_docs = "_2-q8E _2Rdwt"
    Botão_mais = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[5]/div[2]/div/div'
    Botão_reporte = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div/div[2]'
    Botão_cancel = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div'
    Arquivo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div[2]/span/div/div/div/div/div[1]/div/div/div/div'
    
    #Nome das classes aqui (BeautifulSoup )
    #Campo_grupo = "_1Flk2 _3xysY"
    Campo_grupo = "JnmQF _3QmOg"
    Bloco_contato = "_2aBzC"
    Nome_contato = "_35k-1 _1adfa _3-8er"
    
    def __init__(self, PATH_driver, mes):
        self.PATH = PATH_driver
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com')
        self.mes = mes
        
    def __buscarContatos__(self, contato):
        
        search = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_pesquisa)))
        
        actions = ActionChains(self.driver)
        actions.click(search)
        search.clear()
        actions.send_keys_to_element(search, self.contato)
        actions.send_keys_to_element(search, Keys.ENTER)
        
        actions.perform()
    
    def __enviarMensagem__(self):
        
        texto = self.driver.find_element_by_xpath(Zebrinha.Barra_mensagem)
        
        actions1 = ActionChains(self.driver)
        texto.clear()
        actions1.send_keys_to_element(texto, self.definir_Mensagem())
        actions1.send_keys_to_element(texto, Keys.ENTER)
        
        actions1.perform()

    def fechar(self):
        self.driver.close()
        try:
            print(f'Envio feito para {self.num} contatos realizado com sucesso! ;)')
            print(f'Volte sempre att: Zebrinha')
        except:
            print(f'Terminei a tarefa! seu computador está disponível agora ...')
            print(f'Volte sempre att: Zebrinha')

    #Esta com problema em encontrar grupos com mais de 20 contatos
    def buscarContatos_byGroup(self, Nome_Grupo, grupo_Grande=False):
        
        '''
        
        Encontra os nomes dos contatos que participam do grupo. 
        Ainda estamos trabalhando em soluções para grupos com mais de 20 pessoas.
        Caso queira testar a funcionalidade alpha grupo_grande=True.
        
        Parameters
        ----------
        Nome_Grupo : string
            Nome do grupo que deseja pesquisar as pessoas.
        grupo_Grande: boolean
            Tenta achar contatos com grupos com de mais 20 pessoas.

        Returns
        -------
        pessoas_grupo : Lista
            Nome dos contatos que participam do grupo.

        '''
        
        search = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_pesquisa)))
        search.click()
        search.clear()
        search.send_keys(Nome_Grupo)
        search.send_keys(Keys.ENTER)
        
        ID_grupo = self.driver.find_element_by_xpath(Zebrinha.Barra_grupo)
        ID_grupo.click()
        
        try:
            #Espera a barra da ação aparecer e clica no ativo.
            more = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, Zebrinha.Botão_mais)))
            more.click()
            print('Consegui acessar mais contatos! :)')
        except:
            print('Não consegui acessar mais contatos! :(')
            
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        contat_grupo = soup.find(class_= Zebrinha.Campo_grupo)
        blocos = contat_grupo.find_all(class_= Zebrinha.Bloco_contato)
        
        pessoas_grupo = []
        for bloco in blocos:
            pessoas_grupo.append((bloco.find(class_= Zebrinha.Nome_contato).text))
            
        if grupo_Grande:
            Reportar = self.driver.find_element_by_xpath(Zebrinha.Botão_reporte)
            Reportar.click()
            
            Cancelar = self.driver.find_element_by_xpath(Zebrinha.Botão_cancel)
            Cancelar.click()
            
            #Recarregar a página p/ aparecer os contatos
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            contat_grupo = soup.find(class_= Zebrinha.Campo_grupo)
            blocos = contat_grupo.find_all(class_= Zebrinha.Bloco_contato)
            
            for bloco in blocos:
                pessoas_grupo.append((bloco.find(class_= Zebrinha.Nome_contato).text))
            
        try:
            pessoas_grupo.remove('You')
        except:
            pass
        
        pessoas_grupo = sorted(pessoas_grupo) 
        pessoas_grupo = pd.DataFrame(data=pessoas_grupo)
        pessoas_grupo = pessoas_grupo.drop_duplicates()
        
        return pessoas_grupo
    
    #O Google esta atualmente me bloqueando!
    def buscar_Docs(self, contatos):
        
        for self.contato in contatos:
            search = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_pesquisa)))
            
            search.click()
            search.clear()
            
            search.send_keys(self.contato)
            search.send_keys(Keys.ENTER)
            
            Barra_contato = self.driver.find_element_by_xpath(Zebrinha.Barra_grupo)
            Barra_contato.click()
            
            #Problema aqui: NOT LOCATED
            try:
                click_Docs = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, Zebrinha.Barra_docs)))
                click_Docs.click()
            except:
                pass
            
            Docs = self.driver.find_element_by_class_name(Zebrinha.Botão_docs)
            Docs.click()
            
            try:
                Baixar_documento = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, Zebrinha.Arquivo)))
                Baixar_documento.click()
                Baixar_documento.send_keys(Keys.ENTER)
            except:
                pass
            
    def enviar_Msg_fromExcel(self, posição_seuNome, local_excel, Preencher_NaN=True):
        '''
        Envia mensagem para os cantatos e utilizando informações contidas em um arquivo excel. 
        Definida no método definir_Mensagem para a lista de contatos.

        Parameters
        ----------
        posição_seuNome : int
            Posição de onde esta seu nome no arquivo.
        local_excel : PATH
            Local onde esta com final '.xlsx'. Exemplo: 'D:/UNESP/Dados/caixinha.xlsx'.
        Preencher_NaN : Boolean, optional
            Completar as células vázias com 'não pago'. The default is True.

        Returns
        -------
        None.

        '''
        tabela = pd.read_excel(local_excel)
        tabela = tabela.replace('pago  ', 'pagou') # ERRO: 'pago' verificar com financeiro
        tabela = tabela.drop(posição_seuNome)
        
        if Preencher_NaN:
            tabela = tabela.fillna('não pagou')
        
        self.num = 0        
        for self.contato, self.situação in zip(tabela['Nome'], tabela[self.mes]):
            self.__buscarContatos__(self.contato)
            self.__enviarMensagem__()
            self.num += 1
                 
    def enviar_Msg_fromlista(self, Lista_contatos):
        '''
        Envia mensagem definida no método definir_Mensagem para a lista de contatos.
        
        Parameters
        ----------
        Lista_contatos : Lista ou array
            Coloque a lista de contatos que deseja enviar 
            as mensagens. Ex: contatos = ['Arthur', 'Rafael', 'Rebeca']. Importante 
            colocar '[ ... ]'.

        Returns
        -------
        None.
        '''
        self.num = 0        
        for self.contato in Lista_contatos:
            self.__buscarContatos__(self.contato)
            self.__enviarMensagem__()
            self.num += 1
               
    def definir_Mensagem(self):
        return  f''' 
        
        Olá, {self.contato} vc {self.situação} o mês de {self.mes} att: Zebrinha agiota
        ;)
        
    
        '''

#------------------------ PROGRAME AQUI - EXPLEMPLO DE CÓDIGO -----------------------

PATH = 'C:/Users/arthu/Downloads/chromedriver_win32/chromedriver.exe'   
Zb = Zebrinha(PATH, 'março')
Local = 'D:/UNESP/AeroDesign/Códigos_Python/Dados/caixa_auto.xlsx'
Zb.enviar_Msg_fromExcel(1, Local, True)
Zb.fechar()

