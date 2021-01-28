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
ativo = ''
valor = 0
acao = ''
tempo = 0
martingale = ''
martingale_op = 0
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
    print('b) Abir ordem manualmente')
    print()
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
            martingale = 0

            print('*Abrindo ordem!*')
            try:
                ativo = (str(input('Selecione o ativo: ')).strip().upper())
                valor = (int(input('Valor de entrada: ')))
                acao = (str(input('Selecione o call or put: ')).strip())
                tempo = (int(input('Tempo de operação [1/5/10/15]: ')))
                martingale = (str(input('Deseja fazer martingale? [S/n]'))).strip().upper()

                while martingale_op != 2:
                    check, id = iq.buy(valor, ativo, acao, tempo)

                    if check:
                        print('\nCompra Realizada!')
                    else:
                        print('\nErro na compra')
                        break

                    print('\n---Verificando se ganhou!---')
                    if iq.check_win_v3(id) > 0:
                        print('Win')
                        break
                    elif iq.check_win_v3(id) == 0:
                        print('Empate')
                        break
                    else:
                        print('Loss')
                        if martingale in 'Nn':
                            break
                        elif martingale in 'Ss':
                            valor *= 2
                            martingale_op += 1
                            print('Executando Gale', martingale_op)
                        else:
                            break


            except:
                print('O correu um erro na compra!')
            input('Aperte enter!')
            clear()   

        elif select in 'Zz':
            clear()
            break

        else:
            print('Opção inválida')    

else:
    print('Falha no login')    
    