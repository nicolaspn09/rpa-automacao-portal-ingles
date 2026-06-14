import os
import time
import psutil
import tempfile
import requests
import PIL.Image
import urllib.parse
import subprocess
from dotenv import load_dotenv
from selenium import webdriver
from datetime import datetime
import google.generativeai as genai
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Função para matar processos pelo PID
def kill_process(pid):
    pass # Logica de negocio removida por seguranca corporativa

def find_chrome_processes(ppid):
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base_api():
    pass # Logica de negocio removida por seguranca corporativa

def informa_retorno_sheet(linha, informacao):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_gemini(caminho_imagem):
    pass # Logica de negocio removida por seguranca corporativa

def acessa_navegador():
    pass # Logica de negocio removida por seguranca corporativa

def retorna_pagina_principal(navegador):
    pass # Logica de negocio removida por seguranca corporativa

def aceita_cookie(navegador):
    pass # Logica de negocio removida por seguranca corporativa

def informa_usuario_senha(navegador):
    pass # Logica de negocio removida por seguranca corporativa

def aguarda_elementos_principais(navegador):
    pass # Logica de negocio removida por seguranca corporativa

def aguarda_elementos_books(navegador, tipo_livro, livro):
    pass # Logica de negocio removida por seguranca corporativa

def busca_lesson(navegador, lesson):
    pass # Logica de negocio removida por seguranca corporativa



def acessa_lesson(navegador, linha):
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    tabela_base = solicita_tabela_base_api()

    for i in tabela_base:
        linha = i["linha"]
        tipo_livro = i["tipoLivro"]
        livro = i["livro"]
        lesson = i["lesson"]
        informacao = i["informacaoTela"]

        if informacao == "NA":
            navegador, chrome_pids = acessa_navegador()
            informa_usuario_senha(navegador=navegador)
            aguarda_elementos_principais(navegador=navegador)

            aguarda_elementos_books(navegador=navegador, tipo_livro=tipo_livro, livro=livro)
            busca_lesson(navegador=navegador, lesson=lesson)
            #aceita_cookie(navegador=navegador)
            acessa_lesson(navegador=navegador, linha=linha)

            time.sleep(1)

            navegador.quit()