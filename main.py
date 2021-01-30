#Importando API
from iqoptionapi_master import iqoptionapi
from iqoptionapi.stable_api import IQ_Option

#Importando demais bibliotecas
from tkinter import *
import os
import getpass
import time
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
lista_sinais = list()

meta = float()
porcentagem_meta = 0.02
saldo = 0
dinheiro_ganho = float()
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
def menu(porcentagem):
    barrinha = len(iq.get_currency()) + len(str(iq.get_balance())) + len(mode)

    saldo = float(iq.get_balance())
    meta = saldo * porcentagem

    print(f'{datetime.today()}')
    print('-' * (barrinha + 2))
    print(f'{iq.get_currency()} {iq.get_balance()} {mode}')
    print('-' * (barrinha + 2))
    print(f'Meta de hoje: {iq.get_currency()} {meta:.2f}\n')

    print('a) Trocar modo')
    print('c) Alterar meta')
    print()
    print('b) Abir ordem manualmente')
    print('d) importar lista sinais')
    print()
    print('e) EXECUTAR SINAIS*')
    print('f) EXECUTAR MHI*')
    print()
    print('z) Sair')
    print()
    print('Selecione a opção: ')

    return meta


def limpar():
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


def carregar_sinais():
    arquivo = open('sinais.txt', encoding='UTF-8')
    lista = arquivo.read()
    arquivo.close

    lista = lista.split(',')
    
    for index, a in enumerate(lista):
        if a == '':
            del lista[index]

    return lista


def comprar(value,active,action,time):
    check, id = iq.buy(valor, ativo, acao, tempo)

    if check:
        print('\nCompra Realizada!')
    else:
        print('\nErro na compra')

    return check, id


def verificar_win(id):

    print('--Verificando vitória!--')
    if iq.check_win_v3(id) > 0:
        print('Win')
        status = 'win'
    elif iq.check_win_v3(id) == 0:
        print('Empate')
        status = 'tie'
    else:
        print('loss')
        status = 'loss'

    return status    

limpar()

if check == True:
    while True:
        meta = menu(porcentagem_meta)
        select = str(input('->')).strip().upper()

        if select in 'Aa':
            mode = changemode(mode)
            limpar()

        elif select in 'Bb':
            martingale = 0

            print('\n*Abrindo ordem!*')
            try:
                ativo = (str(input('Selecione o ativo: ')).strip().upper())
                valor = (int(input('Valor de entrada: ')))
                acao = (str(input('Selecione o call or put: ')).strip())
                tempo = (int(input('Tempo de operação [1/5/10/15]: ')))
                martingale = (str(input('Deseja fazer martingale? [S/n]'))).strip().upper()

                while martingale_op == 3:
                    
                    check, id = comprar(valor, ativo, acao, tempo)
                    if check == True:
                        statuscompra = verificar_win(id)
                        if statuscompra in 'tie' or statuscompra in 'win':
                            break
                        elif statuscompra in 'loss':
                            if martingale in 'Ss':
                                valor *= 2
                                martingale_op += 1
                                print('Executando Gale', martingale_op)
                        else:
                            break

            except:
                print('O correu um erro na compra!')
            input('Aperte enter!')
            limpar()  

        elif select in 'Cc':
            print(f'Alterando meta, meta atual é {porcentagem_meta*100:.0f}%')
            try:
                porcentagem_meta = int(input('Digite a nova meta em porcento: '))
                if porcentagem_meta <= 0:
                    print('Não pode ser zero ou menor que zero')
                    porcentagem_meta = 0.02
                elif porcentagem_meta > 0:
                    print('Meta alterada')
                    porcentagem_meta = porcentagem_meta / 100   
            except:
                print('Ocorreu um erro')

        elif select in 'Dd':
            try:
                lista_sinais = carregar_sinais()
                print(lista_sinais)
                print('Lista importada com sucesso')
                select = str(input('Deseja Prosseguir? [S/n]')).strip().upper()[0]
                if select in 'Nn':
                    lista_sinais.clear()
                    print('Lista apagada')
            except:
                print('Ocorreu um erro!')  

        elif select in 'Ee':
            if len(lista_sinais) < 5:
                print('Lista inválida ou não importada.')
            else:
                print('Executando lista!')
                while True:
                    hora = datetime.now()
                    hora = str(hora)
                    
                    if lista_sinais[0] in hora:
                        ativo = (str(lista_sinais[1]).strip().upper())
                        valor = (int(lista_sinais[3]))
                        acao = (str(lista_sinais[2]))
                        tempo = (int(lista_sinais[4]))
                        while martingale_op != 3:
                            print('Entrada executada')
                            print(lista_sinais[0:5])
                            
                            check, id = comprar(valor, ativo, acao, tempo)
                            statuscompra = verificar_win(id)

                            if statuscompra in 'tie' or os.stat_result in 'win':
                                dinheiro_ganho += iq.check_win_v3(id)
                                del lista_sinais[0:5]
                                break
                            else:
                                valor *= 2
                                martingale_op += 1
                                if martingale_op == 3:
                                    print('Stop loss')
                        if martingale_op == 3:
                            break            
                        ativo = ''
                        valor = 0
                        acao = ''
                        tempo = 0
                        martingale_op = 0        
                        
                        if dinheiro_ganho >= meta:
                            break

        elif select in 'Ff':
            ativo = str(input(' Indique uma paridade para operar: ')).strip().upper()
            valor = float(input(' Indique um valor para entrar: '))
            meta = float(meta)
            while True:
                minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
                entrar = True if (minutos >= 4.58 and minutos <= 5) or minutos >= 9.58 else False
                limpar()
                print(f'Capturando e análisando velas, Minutos: {minutos}')
                
                if dinheiro_ganho >= meta:
                    print(f'Meta {iq.get_currency()} {meta}')
                    print(f'Meta batida, lucro: {iq.get_currency()} {dinheiro_ganho}')
                    break

                if entrar:
                    print('\n\nIniciando operação!')
                    acao = False
                    print('Verificando cores..', end='')
                    velas = iq.get_candles(ativo, 60, 3, time.time())
                    
                    velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
                    velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
                    velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'
                    
                    cores = velas[0] + ' ' + velas[1] + ' ' + velas[2]		
                    print(cores)
                
                    if cores.count('g') > cores.count('r') and cores.count('d') == 0 : acao = 'put'
                    if cores.count('r') > cores.count('g') and cores.count('d') == 0 : acao = 'call'
                    
                    
                    if acao:
                        
                        print('Direção:',acao)
                        while True:
                            check, id = comprar(valor, ativo, acao, 1)

                            statuscompra = verificar_win(id)


                            if statuscompra in 'win' or statuscompra in 'tie':
                                dinheiro_ganho += iq.check_win_v3(id)
                                break
                            else:
                                valor *= 2
                                martingale_op += 1
                                if martingale_op == 3: 
                                    martingale_op = 0
                                    print('STOP_LOSS!!')
                                    break

                time.sleep(0.5)      

        elif select in 'Zz':
            limpar()
            break

        else:
            print('Opção inválida')    

else:
    print('Falha no login')    
    