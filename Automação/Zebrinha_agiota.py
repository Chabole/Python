# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:01:26 2021

@author: Arthur Chabole
========================

"""

import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup 

class Zebrinha:
    
    #Tempo de espera em segundos
    tempo = 0.2
    
    #Colocar os XPATH aqui (selenium)
    Barra_pesquisa = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    Barra_mensagem = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    Barra_grupo = '//*[@id="main"]/header/div[2]/div[1]/div/span'
    Botão_mais = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[5]/div[2]/div/div'
    Botão_reporte = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div/div[2]'
    Botão_cancel = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div'
    Barra_docs = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[2]/div[2]/div/div[1]/div[1]'
    
    Botão_docs = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div[1]/button[2]'
    Arquivo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div[2]/span/div/div/div/div/div[1]/div/div/div/div'
    
    #Nome das classes aqui (BeautifulSoup )
    #Campo_grupo = "_1Flk2 _3xysY"
    Campo_grupo = "JnmQF _3QmOg"
    Bloco_contato = "_2aBzC"
    Nome_contato = "_35k-1 _1adfa _3-8er"
    
    def __init__(self, PATH_driver):
        self.PATH = PATH_driver
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com')
        
    def fechar(self):
        self.driver.close()

    #Esta com problema em encontrar todos os contatos
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
        
        search = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_pesquisa)))
        search.click()
        search.clear()
        search.send_keys(Nome_Grupo)
        time.sleep(Zebrinha.tempo)
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
        
        return pessoas_grupo
    
    def buscar_Docs(self, contatos):
        
        for self.contato in contatos:
            search = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_pesquisa)))
            
            search.click()
            search.clear()
            
            search.send_keys(self.contato)
            time.sleep(Zebrinha.tempo)
            search.send_keys(Keys.ENTER)
            
            Barra_contato = self.driver.find_element_by_xpath(Zebrinha.Barra_grupo)
            Barra_contato.click()
            
            #Problema aqui: NOT LOCATED
            try:
                click_Docs = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_docs)))
                click_Docs.click()
            except:
                pass
            
            Docs = self.driver.find_element_by_xpath(Zebrinha.Botão_docs)
            Docs.click()
            
            try:
                Baixar_documento = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, Zebrinha.Arquivo)))
                Baixar_documento.click()
                Baixar_documento.send_keys(Keys.ENTER)
            except:
                pass
            
    def enviar_Mensagem(self, contatos):
        
        '''
        
        Envia mensagem definida no método definir_Mensagem para a lista de contatos.
        
        Parameters
        ----------
        contatos : Lista ou array
            Coloque a lista de contatos que deseja enviar 
            as mensagens. Ex: contatos = ['Arthur', 'Rafael', 'Rebeca']. Importante 
            colocar '[ ... ]'.

        Returns
        -------
        None.

        '''
        for self.contato in contatos:
            search = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Zebrinha.Barra_pesquisa)))
            
            search.click()
            search.clear()
            
            search.send_keys(self.contato)
            time.sleep(Zebrinha.tempo)
            search.send_keys(Keys.ENTER)
            
            texto = self.driver.find_element_by_xpath(Zebrinha.Barra_mensagem)
            texto.clear()
            texto.send_keys(self.definir_Mensagem())
            texto.send_keys(Keys.ENTER)
        
    def definir_Mensagem(self):
        msg = f''' 
        
        Olá, {self.contato} tudo bem ? To testando meu robozinho! IGNORE ;)
        
        '''
        return msg
            

    
PATH = 'C:/Users/arthu/Downloads/chromedriver_win32/chromedriver.exe'    
Zb = Zebrinha(PATH)

#Contatos = Zb.buscarContatos_byGroup('Aqui o choro é livre')

Contatos = ['Lele Prima', 'Wine queen']

Zb.buscar_Docs(Contatos)
Zb.fechar()

