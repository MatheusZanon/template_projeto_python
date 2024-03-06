# =========================IMPORTAÇÕES DE BIBLIOTECAS E COMPONENTES========================
from components.importacao_diretorios_windows import listagem_pastas, listagem_arquivos,listagem_arquivos_downloads, pega_nome
from components.extract_text_pdf import extract_text_pdf
from components.importacao_caixa_dialogo import DialogBox
from components.checar_ativacao_google_drive import checa_google_drive
from components.configuracao_db import configura_db, ler_sql
from components.procura_cliente import procura_cliente
from components.procura_valores import procura_valores, procura_valores_com_codigo
from components.procura_elementos_web import procura_elemento, procura_todos_elementos, encontrar_elemento_shadow_root
from components.configuracao_selenium_drive import configura_selenium_driver
from components.enviar_emails import enviar_email_com_anexos
import tkinter as tk
import mysql.connector
from re import search
from pathlib import Path
from shutil import copy
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, NamedStyle
import win32com.client as win32
from dotenv import load_dotenv
import os
from time import sleep, time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import  NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

