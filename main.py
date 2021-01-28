#Importando API
from iqoptionapi_master import iqoptionapi
from iqoptionapi.stable_api import IQ_Option

#Importando demais bibliotecas
from tkinter import *
import os
import getpass
from datetime import datetime
from dateutil import tz

# Declarando variáveis
login = ''
password = ''
select = ''
mode = 'PRACTICE'
# Sistema Login
def login():
    log = str(input('Digite Seu login: ')).strip()
    passwd = getpass.getpass('Digite sua senha: ')

    print('Efetuando Login aguarde!')

    return log, passwd


login, password = login()

iq = IQ_Option(login, password)

check, reason = iq.connect()

# Funções
def menu():
    barrinha = len(iq.get_currency()) + len(str(iq.get_balance())) + len(mode)

    print('-' * (barrinha + 2))
    print(f'{iq.get_currency()} {iq.get_balance()} {mode}')
    print('-' * (barrinha + 2))

    print('a) Trocar modo')
    print('z) Sair')
    print()
    print('Selecione a opção: ')


def clear():
    if os.name in "nt":
        os.system("cls")
    else:
        os.system("clear")


def changemode(mode_f):
    if mode_f == 'PRACTICE':
        mode_f = 'REAL'
        iq.change_balance(mode_f)
    else:
        mode_f = 'PRACTICE'
        iq.change_balance(mode_f)
    return mode_f        


if check == True:
    while True:
        menu()
        select = str(input('->')).strip().upper()

        if select in 'Aa':
            mode = changemode(mode)
            clear()
        elif select in 'Bb':
            print('Abrindo ordem!')    
        elif select in 'Zz':
            clear()
            break
        else:
            print('Opção inválida')    

else:
    print('Falha no login')    