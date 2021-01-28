#Importando API
from iqoptionapi_master import iqoptionapi
from iqoptionapi.stable_api import IQ_Option

#Importando demais bibliotecas
from tkinter import *
import getpass
from datetime import datetime
from dateutil import tz

# Declarando variáveis
login = ''
password = ''

def login():
    log = str(input('Digite Seu login: ')).strip()
    passwd = getpass.getpass('Digite sua senha: ')

    print('Efetuando Login aguarde!')

    return log, passwd


login, password = login()

iq = IQ_Option(login, password)

check, reason = iq.connect()

if check == True:
    print('Bem-vindo!')
    input('Pressione enter!')
    
else:
    print('Erro no Login!')
    
